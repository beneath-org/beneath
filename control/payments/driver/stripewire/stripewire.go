package stripewire

import (
	"fmt"
	"net/http"

	"gitlab.com/beneath-hq/beneath/control/entity"
	"gitlab.com/beneath-hq/beneath/control/payments/driver"
	"gitlab.com/beneath-hq/beneath/control/payments/driver/stripeutil"
	"gitlab.com/beneath-hq/beneath/internal/middleware"
	"gitlab.com/beneath-hq/beneath/pkg/envutil"
	"gitlab.com/beneath-hq/beneath/pkg/httputil"
	"gitlab.com/beneath-hq/beneath/pkg/log"
	uuid "github.com/satori/go.uuid"
	stripe "github.com/stripe/stripe-go"
)

// StripeWire implements beneath.PaymentsDriver
type StripeWire struct {
	config configSpecification
}

type configSpecification struct {
	StripeSecret        string `envconfig:"CONTROL_STRIPE_SECRET" required:"true"`
	PaymentsAdminSecret string `envconfig:"CONTROL_PAYMENTS_ADMIN_SECRET" required:"true"`
}

// New initializes a StripeWire object
func New() StripeWire {
	var config configSpecification
	envutil.LoadConfig("beneath", &config)
	stripeutil.InitStripe(config.StripeSecret)
	return StripeWire{
		config: config,
	}
}

// GetHTTPHandlers returns the necessary handlers to implement Stripe card payments
func (s *StripeWire) GetHTTPHandlers() map[string]httputil.AppHandler {
	return map[string]httputil.AppHandler{
		"initialize_customer": s.handleInitializeCustomer,
		// "webhook":               handleStripeWebhook,       // TODO: when a customer pays by wire, check to see if any important Stripe events are emitted via webhook
		"get_payment_details": s.handleGetPaymentDetails,
	}
}

// create/update a customer's billing info and Stripe registration
func (s *StripeWire) handleInitializeCustomer(w http.ResponseWriter, req *http.Request) error {
	organizationID, err := uuid.FromString(req.URL.Query().Get("organizationID"))
	if err != nil {
		return httputil.NewError(400, "couldn't get organizationID from the request")
	}

	organization := entity.FindOrganization(req.Context(), organizationID)
	if organization == nil {
		return httputil.NewError(400, "organization not found")
	}

	billingPlanID, err := uuid.FromString(req.URL.Query().Get("billingPlanID"))
	if err != nil {
		return httputil.NewError(400, "couldn't get billingPlanID from the request")
	}

	billingPlan := entity.FindBillingPlan(req.Context(), billingPlanID)
	if billingPlan == nil {
		return httputil.NewError(400, "billing plan not found")
	}

	emailAddress := req.URL.Query().Get("emailAddress")
	if emailAddress == "" {
		return httputil.NewError(400, "couldn't get emailAddress from the request")
	}

	// Beneath will call the function from an admin panel (after a customer discussion)
	secret := middleware.GetSecret(req.Context())
	if secret.GetSecretID().String() != s.config.PaymentsAdminSecret {
		return httputil.NewError(403, fmt.Sprintf("Enterprise plans require a Beneath Payments Admin to activate"))
	}

	// Our requests to Stripe differ whether or not the customer is already registered in Stripe
	var customer *stripe.Customer
	driverPayload := make(map[string]interface{})
	billingInfo := entity.FindBillingInfo(req.Context(), organization.OrganizationID)
	if billingInfo.DriverPayload["customer_id"] != nil {
		// customer is already registered with Stripe
		driverPayload["customer_id"] = billingInfo.DriverPayload["customer_id"]
		stripeutil.UpdateWireCustomer(driverPayload["customer_id"].(string), emailAddress)
	} else {
		// customer needs to be registered with stripe
		customer = stripeutil.CreateWireCustomer(organization.OrganizationID, organization.Name, emailAddress)
		driverPayload["customer_id"] = customer.ID
	}

	_, err = entity.UpdateBillingInfo(req.Context(), organization.OrganizationID, billingPlan.BillingPlanID, entity.StripeWireDriver, driverPayload)
	if err != nil {
		log.S.Errorf("Error updating billing info: %v\\n", err)
		return httputil.NewError(500, "error updating billing info: %v\\n", err)
	}

	return nil
}

func (s *StripeWire) handleGetPaymentDetails(w http.ResponseWriter, req *http.Request) error {
	// TODO: is there anything we want to return to the front-end?
	// - bank account information where the wire should be sent
	// - state of recent payment (paid, X days remaining, Y days overdue)
	return nil
}

// IssueInvoiceForResources implements Payments interface
func (s *StripeWire) IssueInvoiceForResources(billingInfo driver.BillingInfo, billedResources []driver.BilledResource) error {
	inv := stripeutil.CreateStripeInvoice(billingInfo, billedResources)
	stripeutil.SendInvoice(inv.ID)

	return nil
}
