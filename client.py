import asyncio
import nest_asyncio
from mcp import ClientSession
from mcp.client.sse import sse_client

async def main():
    # Connect to the server using SSE
    endpoint = "include-operations-mcp"
    async with sse_client(f"http://localhost:8123/{endpoint}") as (read_stream, write_stream):
        async with ClientSession(read_stream, write_stream) as session:
            # Initialize the connection
            await session.initialize()

            # List available tools
            # tools_result = await session.list_tools()
            tools_result = await session.list_tools()
            # print(tools_result.tools[1])
            # tool_list = [
            #     {
            #         "type": "function",
            #         "function": {
            #             "name": tool.name,
            #             "description": tool.description,
            #             "parameters": tool.inputSchema,
            #         },
            #     }
            #     for tool in tools_result.tools
            # ]
            # print(tool_list)
            for tool in tools_result.tools[1:2]:
                print(f"Tool Name: {tool.name}")
                print(f"Description: {tool.description}")
                print(f"Parameters: {tool.inputSchema}")
                break


if __name__ == "__main__":
    asyncio.run(main())