import Page from "../components/Page";
import { MainSidebar } from "../components/Sidebar";

export default () => (
  <Page title="Profile" sidebar={<MainSidebar />}>
    <div className="section">
      <div className="title">
        <h1>Profile</h1>
      </div>
      {/* 
        Section 1: Edit name and bio
        Section 2: Create new API key -- readonly (green) or readwrite (red)
        Section 3: View all API keys (show type)
      */}
    </div>
  </Page>
);
