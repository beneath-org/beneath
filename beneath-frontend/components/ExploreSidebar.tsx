import { SingletonRouter, withRouter } from "next/router";
import { FC } from "react";

import List from "@material-ui/core/List";
import ListItem from "@material-ui/core/ListItem";
import ListItemAvatar from "@material-ui/core/ListItemAvatar";
import ListItemText from "@material-ui/core/ListItemText";
import ListSubheader from "@material-ui/core/ListSubheader";
import { makeStyles } from "@material-ui/core/styles";

import { Me } from "../apollo/types/Me";
import withMe from "../hocs/withMe";
import Avatar from "./Avatar";
import NextMuiLink from "./NextMuiLink";

const useStyles = makeStyles((theme) => ({
  listItemAvatar: {
    minWidth: theme.spacing(0),
  },
}));

interface IListEntryProps {
  href: string;
  as?: string;
  label: string;
  selected: boolean;
  showAvatar?: boolean;
  photoURL?: string | null;
}

const ListEntry: FC<IListEntryProps> = ({ href, as, label, selected, showAvatar, photoURL }) => {
  const classes = useStyles();
  return (
    // @ts-ignore: https://github.com/mui-org/material-ui/issues/14970
    <ListItem button selected={selected} component={NextMuiLink} as={as} href={href}>
      {showAvatar && (
        <ListItemAvatar className={classes.listItemAvatar}>
          <Avatar size="dense-list" label={label} src={photoURL || ""} />
        </ListItemAvatar>
      )}
      <ListItemText primary={label} />
    </ListItem>
  );
};

interface IExploreSidebarProps extends Me {
  router: SingletonRouter;
}

const ExploreSidebar: FC<IExploreSidebarProps> = ({ me, router }) => {
  const selected = (pathRegex: RegExp) => !!router.asPath.match(pathRegex);
  return (
    <div>
      <List dense>
        <ListSubheader>Home</ListSubheader>
        <ListEntry key={"/explore"} href={"/explore"} label={"Explore"}
          selected={selected(/^\/explore/)} />
        <ListEntry key={"/users/me"} href={"/user?id=me"} as={"/users/me"} label={"My profile"}
          selected={selected(/^\/users\/me/)} />

        <ListSubheader>Create</ListSubheader>
        <ListEntry key={"/new/project"} href={"/new/project"} label={"New project"}
          selected={selected(/^\/new\/project/)} />
        <ListEntry key={"/new/external-stream"} href={"/new/external-stream"} label={"New external stream"}
          selected={selected(/^\/new\/external-stream/)} />

        {me && (
          <>
            <ListSubheader>My projects</ListSubheader>
            {me.user.projects.map((project) => (
              <ListEntry
              key={`/project?name=${project.name}`}
              href={`/project?name=${project.name}`}
              as={`/projects/${project.name}`}
              label={project.displayName}
              selected={selected(new RegExp(`^/projects/${project.name}`))}
              photoURL={project.photoURL}
              showAvatar
            />
            ))}
          </>
        )}
      </List>
    </div>
  );
};

export default withMe(withRouter(ExploreSidebar));