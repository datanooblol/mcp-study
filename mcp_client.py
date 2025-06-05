
import asyncio
import nest_asyncio
from mcp import ClientSession
from mcp.client.sse import sse_client
from mcp import types
import json

async def main():
    # Connect to the server using SSE
    endpoint = "sse"
    async with sse_client(f"http://localhost:8000/{endpoint}") as (read_stream, write_stream):
        async with ClientSession(read_stream, write_stream) as session:
            await session.initialize()

            tools_results = await session.list_tools()
            print("Available Tools:", tools_results.tools)
            # echo = await session.call_tool("echo", arguments={"banana": "Hello, MCP!"})
            # print("Echo Tool Result:", echo)
            print("="*20)

            # resources_results = await session.list_resources()
            # print("Available Resources:", resources_results.resources)
            # list_resources = await session.read_resource(uri="resources://list")
            # resource = json.loads(list_resources.contents[0].text)
            # resource = types.Resource(**resource[0])
            # print("Resource URI:", resource.uri)
            # print("Resource Name:", resource.name)
            # print("Resource MIME Type:", resource.mimeType)

            # config = await session.read_resource("config://app")
            # print("Config Resource:", config)
            # greeting = await session.read_resource("greeting://Alice")
            # print("Greeting Resource:", greeting)
            # settings = await session.read_resource("users://123/settings")
            # print("User Settings Resource:", settings)
            # print("="*20)

            # prompts_results = await session.list_prompts()
            # print("Available Prompts:", prompts_results.prompts)
            # review_code = await session.get_prompt("review_code", arguments={"code": "print('Hello, World!')"},)
            # print("Prompt Result:", review_code)
            # print(review_code.messages[0].content.text)
            # debug_error = await session.get_prompt("debug_error", arguments={"error": "IndexError: list index out of range"})
            # print("Debug Error Result:", debug_error)

if __name__ == "__main__":
    asyncio.run(main())