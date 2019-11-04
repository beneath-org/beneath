import { useMutation, useQuery } from "@apollo/react-hooks";
import React, { FC } from "react";
import Moment from "react-moment";

import { IconButton, List, ListItem, ListItemSecondaryAction, ListItemText } from "@material-ui/core";
import DeleteIcon from "@material-ui/icons/Delete";

import { QUERY_USER_SECRETS, REVOKE_USER_SECRET } from "../../apollo/queries/secret";
import { RevokeUserSecret, RevokeUserSecretVariables } from "../../apollo/types/RevokeUserSecret";
import { SecretsForUser, SecretsForUserVariables } from "../../apollo/types/SecretsForUser";
import Loading from "../Loading";

interface ViewSecretsProps {
  userID: string;
}

const ViewSecrets: FC<ViewSecretsProps> = ({ userID }) => {
  const { loading, error, data } = useQuery<SecretsForUser, SecretsForUserVariables>(QUERY_USER_SECRETS, {
    variables: { userID },
  });

  const [revokeSecret, { loading: mutLoading }] = useMutation<RevokeUserSecret, RevokeUserSecretVariables>(
    REVOKE_USER_SECRET
  );

  if (loading) {
    return <Loading justify="center" />;
  }

  if (error || !data) {
    return <p>Error: {JSON.stringify(error)}</p>;
  }

  return (
    <List dense={true}>
      {data.secretsForUser.map(({ createdOn, description, userSecretID, prefix }) => (
        <ListItem key={userSecretID} disableGutters>
          <ListItemText
            primary={
              <React.Fragment>
                {description || <em>No description</em>} (starts with <strong>{prefix}</strong>)
              </React.Fragment>
            }
            secondary={
              <React.Fragment>
                Secret issued <Moment fromNow date={createdOn} />
              </React.Fragment>
            }
          />
          <ListItemSecondaryAction>
            <IconButton
              edge="end"
              aria-label="Delete"
              disabled={mutLoading}
              onClick={() => {
                revokeSecret({
                  variables: { secretID: userSecretID },
                  update: (cache, { data }) => {
                    if (data && data.revokeUserSecret) {
                      const queryData = cache.readQuery({
                        query: QUERY_USER_SECRETS,
                        variables: { userID },
                      }) as any;
                      const filtered = queryData.secretsForUser.filter(
                        (secret: any) => secret.userSecretID !== userSecretID
                      );
                      cache.writeQuery({
                        query: QUERY_USER_SECRETS,
                        variables: { userID },
                        data: { secretsForUser: filtered },
                      });
                    }
                  },
                });
              }}
            >
              <DeleteIcon />
            </IconButton>
          </ListItemSecondaryAction>
        </ListItem>
      ))}
    </List>
  );
};

export default ViewSecrets;
