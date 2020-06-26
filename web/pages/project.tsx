import { useQuery } from "@apollo/react-hooks";
import { useRouter } from "next/router";
import React from "react";

import Loading from "../components/Loading";
import Page from "../components/Page";
import ProfileHero from "../components/ProfileHero";
import SubrouteTabs from "../components/SubrouteTabs";

import EditProject from "../components/project/EditProject";
import ViewMembers from "../components/project/ViewMembers";
import ViewServices from "../components/project/ViewServices";
import ViewStreams from "../components/project/ViewStreams";

import { QUERY_PROJECT } from "../apollo/queries/project";
import { ProjectByOrganizationAndName, ProjectByOrganizationAndNameVariables } from "../apollo/types/ProjectByOrganizationAndName";
import { withApollo } from "../apollo/withApollo";
import ErrorPage from "../components/ErrorPage";
import { toBackendName, toURLName } from "../lib/names";


const ProjectPage = () => {
  const router = useRouter();

  if (typeof router.query.organization_name !== "string" || typeof router.query.project_name !== "string") {
    return <ErrorPage statusCode={404} />;
  }

  const organizationName = toBackendName(router.query.organization_name);
  const projectName = toBackendName(router.query.project_name);
  const title = `${toURLName(organizationName)}/${toURLName(projectName)}`;

  const {
    loading,
    error,
    data,
  } = useQuery<ProjectByOrganizationAndName, ProjectByOrganizationAndNameVariables>(QUERY_PROJECT, {
    fetchPolicy: "cache-and-network",
    variables: { organizationName, projectName },
  });

  if (loading) {
    return (
      <Page title={title} subheader>
        <Loading justify="center" />
      </Page>
    );
  }

  if (error || !data) {
    return <ErrorPage apolloError={error} />;
  }

  const project = data.projectByOrganizationAndName;

  const tabs = [{ value: "streams", label: "Streams", render: () => <ViewStreams project={project} /> }];
  if (project.permissions.view) {
    tabs.push({ value: "members", label: "Members", render: () => <ViewMembers project={project} /> });
  }
  tabs.push({ value: "services", label: "Services", render: () => <ViewServices project={project} /> });
  if (project.permissions.admin) {
    tabs.push({ value: "edit", label: "Edit", render: () => <EditProject project={project} /> });
  }

  return (
    <Page title={title} subheader>
      <ProfileHero
        name={toURLName(project.name)}
        displayName={project.displayName}
        site={project.site}
        description={project.description}
        avatarURL={project.photoURL}
      />
      <SubrouteTabs defaultValue="streams" tabs={tabs} />
    </Page>
  );
};

export default withApollo(ProjectPage);
