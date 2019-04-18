const next = require("next");
const express = require("express");
const connection = require("./lib/connection");
const cookieParser = require("cookie-parser");
const cors = require("cors");
const fetch = require("isomorphic-unfetch");
const helmet = require("helmet");
const compression = require("compression");
const redirectToHTTPS = require("express-http-to-https").redirectToHTTPS;

const port = parseInt(process.env.PORT, 10) || 3000;
const dev = process.env.NODE_ENV !== "production";
const app = next({ dev });
const handle = app.getRequestHandler();

app.prepare().then(() => {
  const server = express();

  // Health check
  server.get("/healthz", (req, res) => {
    res.sendStatus(200);
  });

  // Redirect https
  server.enable("trust proxy");
  server.use(redirectToHTTPS([/localhost:(\d+)/], [], 301));

  // Enable compression
  server.use(compression());

  // Headers security
  server.use(helmet());

  // CORS
  server.use(cors());

  // Parse cookies for logout route
  server.use(cookieParser());

  // Logout
  server.get("/auth/logout", (req, res) => {
    // If the user is logged in, we'll let the backend logout the token (i.e. delete the token from it's registries)
    // Can't do it with a direct <a> on the client because we have to set the token in the header
    let token = req.cookies["token"];
    if (token) {
      let headers = { authorization: `Bearer ${token}` };
      let x = fetch(`${connection.API_URL}/auth/logout`, { headers }).then((r) => {
        console.log(`Successfully logged out ${token}`);
      }).catch((e) => {
        console.error("Error occurred calling backend /auth/logout: ", e);
      });
    }
    res.clearCookie("token");
    res.redirect("/");
  });

  // Redirected to by backend after login
  server.get("/auth/callback/login", (req, res) => {
    let token = req.query.token;
    if (token) {
      res.cookie("token", token);
    } else {
      res.clearCookie("token");
    }
    res.redirect("/");
  });

  // Next.js handlers
  server.get("*", (req, res) => {
    return handle(req, res);
  });

  // Run server
  server.listen(port, err => {
    if (err) throw err;
    console.log(`Ready on ${port}`);
  });
});
