# What an MCP Server Is in Claude Code

MCP servers give Claude Code access to your tools, databases, and APIs [C2]. The docs suggest connecting one when you find yourself copying data into chat from another tool [C5].

## The short version

MCP stands for Model Context Protocol. A protocol is just an agreed set of rules, like a plug shape that lets any device fit any socket. MCP is an open source standard for connecting AI tools to other software [C1]. Claude Code can connect to hundreds of external tools and data sources this way [C1].

An MCP server is the piece on the other side of that plug. Think of it as a small adapter for one service. Once connected, it gives Claude Code access to your tools, databases, and APIs [C2]. (An API is a doorway that lets one program talk to another.)

## Example: from ticket to pull request

Say your team tracks work in JIRA and keeps code on GitHub. With the right servers connected, you can type this to Claude Code: "Add the feature described in JIRA issue ENG-4521 and create a PR on GitHub." [C4] A PR, or pull request, is a proposal to add your changes to a project. Without the servers, you would have to paste the ticket text into the chat yourself.

## How do you know you need one?

The docs give a simple test. Connect a server when you find yourself copying data into chat from another tool, like an issue tracker or a monitoring dashboard [C5].

## Adding one

You add a server with a command in your terminal. For a remote server, the pattern is `claude mcp add --transport http <name> <url>` [C8]. The docs show Notion as their example [C8].

"Transport" here means how Claude Code talks to the server. There are two kinds you will meet first:

- **HTTP** is the recommended choice for remote servers, meaning ones running somewhere else on the internet [C6].
- **Stdio** servers run as local processes on your own machine [C7].

You can also choose where a server's setup applies. There are three scopes: local, project and user, and local is the default [C9].

## One warning

A server is software you are inviting into your workflow, so be choosy. The docs say to verify you trust each server before connecting it [C10]. Servers that fetch outside content can expose you to prompt injection risk [C10]. In plain terms, that means text from a web page or document could contain hidden instructions aimed at the AI rather than at you.

## Sources

- https://code.claude.com/docs/en/mcp
