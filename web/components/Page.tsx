import { Container, makeStyles, Typography } from "@material-ui/core";
import React from "react";

import Drawer from "./Drawer";
import Header from "./Header";
import LinkTypography from "./LinkTypography";
import PageTitle from "./PageTitle";
import Subheader from "./Subheader";

interface IStylesProps {
  contentMarginTop?: null | "dense" | "normal" | "hero";
}

const useStyles = makeStyles((theme) => ({
  container: {
    minHeight: "100vh",
    position: "relative",
  },
  footer: {
    position: "absolute",
    bottom: 0,
    width: "100%",
    padding: theme.spacing(3),
    textAlign: "center",
  },
  sidebarSubheaderAndContent: {
    display: "flex",
  },
  subheaderAndContent: {
    overflow: "auto",
    flexGrow: 1,
    padding: theme.spacing(3),
  },
  content: ({ contentMarginTop }: IStylesProps) => ({
    marginBottom: theme.spacing(12),
    marginTop:
      contentMarginTop === "normal"
        ? theme.spacing(6)
        : contentMarginTop === "dense"
        ? theme.spacing(3)
        : contentMarginTop === "hero"
        ? theme.spacing(10)
        : theme.spacing(0),
  }),
}));

interface IProps {
  title?: string;
  sidebar?: JSX.Element;
  subheader?: boolean;
  maxWidth?: false | "xs" | "sm" | "md" | "lg" | "xl";
  contentMarginTop?: null | "dense" | "normal" | "hero";
}

const Page: React.FC<IProps> = (props) => {
  const [mobileDrawerOpen, setMobileDrawerOpen] = React.useState(false);
  const toggleMobileDrawer = () => {
    setMobileDrawerOpen(!mobileDrawerOpen);
  };

  const classes = useStyles({ contentMarginTop: props.contentMarginTop });
  return (
    <div className={classes.container}>
      <PageTitle title={props.title} />
      <Header toggleMobileDrawer={props.sidebar && toggleMobileDrawer} />
      <div className={classes.sidebarSubheaderAndContent}>
        {props.sidebar && (
          <Drawer mobileOpen={mobileDrawerOpen} toggleMobileOpen={toggleMobileDrawer}>
            {props.sidebar}
          </Drawer>
        )}
        <div className={classes.subheaderAndContent}>
          <Container maxWidth={props.maxWidth || "lg"}>
            {props.subheader && <Subheader />}
            <main className={classes.content}>{props.children}</main>
          </Container>
        </div>
      </div>
      <div className={classes.footer}>
        <Typography variant="body1">
          Powered by Beneath.&nbsp;
          <LinkTypography href="https://about.beneath.dev/policies/terms/">Terms</LinkTypography>.&nbsp;
          <LinkTypography href="https://about.beneath.dev/policies/privacy/">Privacy</LinkTypography>.&nbsp;
          <LinkTypography href="https://about.beneath.dev/contact/">Contact</LinkTypography>.&nbsp;
        </Typography>
      </div>
    </div>
  );
};

export default Page;
