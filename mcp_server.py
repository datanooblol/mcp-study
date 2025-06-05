
from mcp.server.fastmcp import FastMCP
from mcp.server.fastmcp.prompts import base
from mcp import types
from pydantic import Field

mcp = FastMCP("Demo")


# Add an addition tool
# @mcp.tool()
# def add(a: int, b: int) -> int:
#     """Add two numbers"""
#     return a + b

# @mcp.tool()
# def subtract(a: int, b: int) -> int:
#     """Subtract two numbers"""
#     return a - b

@mcp.tool()
def echo(
    message: str = Field(..., description="The message to echo back")
    # message:str
) -> str:
    """Echo a message back"""
    return f"Echo: {message}"

# Add a dynamic greeting resource
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"

@mcp.resource("greeting://default")
def get_default_greeting() -> str:
    """Get a default greeting"""
    return "Hello, World!"

@mcp.resource("config://app")
def get_config() -> str:
    """Static configuration data"""
    return "App configuration here"

@mcp.resource("resources://list")
def list_resources() -> list[types.Resource]:
    """List available resources"""
    return [
        types.Resource(
            uri="retrieve://{search_term}",
            name="Dynamic Data Retrieval",
            mimeType="text/plain"
        ),
    ]

@mcp.resource("retrieve://{search_term}")
def retrieve_data(search_term: str) -> str:
    """Dynamic data retrieval based on search term"""
    return f"Data retrieved for search term: {search_term}"

@mcp.resource("users://{user_id}/settings")
def get_user_settings(user_id: str) -> str:
    """Dynamic user settings"""
    return f"Settings for user {user_id}"


@mcp.resource("users://{user_id}/profile")
def get_user_profile(user_id: str) -> str:
    """Dynamic user data"""
    return f"Profile data for user {user_id}"

@mcp.prompt()
def review_code(code: str) -> str:
    return f"Please review this code:\n\n{code}"

@mcp.prompt()
def debug_error(error: str) -> list[base.Message]:
    return [
        base.UserMessage("I'm seeing this error:"),
        base.UserMessage(error),
        base.AssistantMessage("I'll help debug that. What have you tried so far?"),
    ]

if __name__ == "__main__":
    # Run the MCP server
    mcp.run(transport="sse")