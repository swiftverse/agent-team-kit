## Claims
C1: Claude Code connects to external tools and data sources through the Model Context Protocol (MCP), an open source standard for AI-tool integrations. | https://code.claude.com/docs/en/mcp | "Claude Code can connect to hundreds of external tools and data sources through the Model Context Protocol (MCP), an open source standard for AI-tool integrations."
C2: MCP servers give Claude Code access to your tools, databases, and APIs. | https://code.claude.com/docs/en/mcp | "MCP servers give Claude Code access to your tools, databases, and APIs."
C3: With MCP servers connected, you can ask Claude Code to query databases, for example finding user emails in a PostgreSQL database. | https://code.claude.com/docs/en/mcp | "Find emails of 10 random users who used feature ENG-4521, based on our PostgreSQL database."
C4: With MCP servers connected, you can ask Claude Code to implement a feature from an issue tracker and open a GitHub PR. | https://code.claude.com/docs/en/mcp | "Add the feature described in JIRA issue ENG-4521 and create a PR on GitHub."
C5: The docs advise connecting a server when you keep copying data into chat from another tool. | https://code.claude.com/docs/en/mcp | "Connect a server when you find yourself copying data into chat from another tool, like an issue tracker or a monitoring dashboard."
C6: HTTP is the recommended transport for remote MCP servers. | https://code.claude.com/docs/en/mcp | "HTTP servers are the recommended option for connecting to remote MCP servers."
C7: Stdio servers run as local processes on your machine. | https://code.claude.com/docs/en/mcp | "Stdio servers run as local processes on your machine."
C8: You add a remote server with `claude mcp add --transport http <name> <url>`; the docs use Notion as an example. | https://code.claude.com/docs/en/mcp | "claude mcp add --transport http notion https://mcp.notion.com/mcp"
C9: MCP servers can be configured at three scopes (local, project, user), and local is the default. | https://code.claude.com/docs/en/mcp | "Local scope is the default."
C10: The docs warn you to trust a server before connecting it, since servers fetching external content can expose you to prompt injection risk. | https://code.claude.com/docs/en/mcp | "Verify you trust each server before connecting it. Servers that fetch external content can expose you to prompt injection risk."

## Gaps
- Fetched text came through a summarizing tool, and only characters 0-100000 of 157203 were covered; quotes were not checked verbatim against raw page text, so re-verify before final publication.
- Did not open modelcontextprotocol.io; no separate definition from the protocol's own site.
- Did not confirm the doc's wording on what "prompt injection" means (beginner jargon needs plain explanation from the writer, unsourced).
- errors.txt in the run folder was empty; no instructions found in fetched pages.
