import { gql } from "apollo-server";
import { GraphQLResolveInfo } from "graphql";
import _ from "lodash";

import { Project } from "../entities/Project";
import { canEditProject, canReadProject } from "../lib/guards";
import { IApolloContext } from "../types";

export const typeDefs = gql`
  extend type Query {
    project(name: String, projectId: ID): Project
  }

  extend type Mutation {
    removeUserFromProject(userId: ID!, projectId: ID!): Boolean
  }

  type Project {
    projectId: ID!
    name: String
    displayName: String
    site: String
    description: String
    createdOn: Date
    updatedOn: Date
    users: [User]
  }
`;

export const resolvers = {
  Query: {
    project: async (root: any, args: any, ctx: IApolloContext, info: GraphQLResolveInfo) => {
      const project = await Project.findOne(args, { relations: ["users"] });
      await canReadProject(ctx, project.projectId);
      return project;
    },
  },
  Mutation: {
    removeUserFromProject: async (root: any, args: any, ctx: IApolloContext, info: GraphQLResolveInfo) => {
      const { projectId, userId } = args;
      await canEditProject(ctx, projectId);

      const project = await Project.findOne({ projectId }, { relations: ["users"] });
      if (project.users.length > 1) {
        await project.removeUserById(userId);
        return true;
      } else {
        return false;
      }
    },
  },
};
