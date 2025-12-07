# MCP Server for HNPX Documents

An MCP (Model Context Protocol) server for working with HNPX (Hierarchical Narrative Planning XML) documents. This server provides tools for reading, editing, and analyzing structured fiction documents.

## What is HNPX?

HNPX is a hierarchical XML format for planning and writing fiction. For the complete specification, see [`docs/HNPX.md`](docs/HNPX.md).

## Installation

1. Install the package dependencies:
```bash
pip install -e .
```

2. The server will be available as `hnpx-mcp` command.

## MCP Server Configuration

Add this server to your MCP configuration file:

```json
{
  "mcpServers": {
    "hnpx": {
      "command": "hnpx-mcp",
      "args": [],
      "env": {}
    }
  }
}
```
