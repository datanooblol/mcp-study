from mcp import ClientSession
from mcp.client.sse import sse_client

async def get_tools():
    """Get tools from the server using SSE."""
    endpoint = "include-operations-mcp"
    async with sse_client(f"http://localhost:8123/{endpoint}") as (read_stream, write_stream):
        async with ClientSession(read_stream, write_stream) as session:
            # Initialize the connection
            await session.initialize()
            # List available tools
            tools_result = await session.list_tools()
            return tools_result.tools