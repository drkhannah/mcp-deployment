# Installation

Add the following to your Claude Desktop configuration to enable these MCP servers:

## Configuration

```json
{
  "mcpServers": {
    "mcp-server": {
      "command": "uvx",
      "args": [
        "--from",
        "git+https://github.com/drkhannah/mcp-deployment",
        "mcp-server"
      ]
    }
  }
}
```

## Servers

- **mcp-server**: MCP deployment server
