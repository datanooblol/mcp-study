from fastapi import FastAPI
from fastapi_mcp import FastApiMCP
from typing import Dict, Any, List
from pydantic import BaseModel, Field

app = FastAPI(
    name="My FastAPI",  # Name for your MCP server
    description="FastAPI server",  # Description,
    version="0.1.0",
    openapi_url="/openapi.json"
)

@app.get("/")
def root():
    return {"response": "root"}

@app.get("/home", operation_id="home", response_model=dict[str, Any])
def home(address: str = "Prison")->Dict[str, Any]:
    """An address
    
    Args:
        address: this is an address
        
    Return
        - dict : a dictionary of message
    """
    return {"response": f"home boi {address}"}

@app.get("/protect_secret", operation_id="protect_secret", response_model=dict[str, str])
def protect_secret(secret: str):
    """This is a secret protector
    
    Args:
        secret (str) : an input secret
        
    Return:
        - dict : a dictionary of secret protector
    """
    return {"response": f"Your secret is xxxx"}

class ExposeSecret(BaseModel):
    secret: str = Field(description="a secret to expose")

@app.get("/expose_secret", operation_id="expose_secret", response_model=ExposeSecret)
def expose_secret(secret: str):
    """This is a secret exposure
    
    Args:
        secret (str) : an input secret
        
    Return:
        - dict : a dictionary of secret exposure
    """
    return ExposeSecret(secret=secret)

class Todos(BaseModel):
    todos: List[str] = Field(description="a todo list")

@app.post("/create_todo_list", operation_id="create_todo_list", response_model=dict[str, Any])
def create_todo_list(todos:Todos):
    """Create a todo list
    
    Args:
        session (dict) : a dictionary of {"todos": []}
    
    Retrun:
        - dict : a dictionary of created todos
    """
    return {"resonse": todos.todos}
mcp = FastApiMCP(
    app,  
        include_operations=[
            "home",
            "expose_secret",
            "create_todo_list"
        ],
    name="My API MCP",  # Name for your MCP server
    description="MCP server for my API",  # Description
    describe_all_responses=True,  # Include all possible response schemas
    describe_full_response_schema=True  # Include full JSON schema in descriptions    
)

mcp.mount(
    mount_path="/include-operations-mcp"
    )
mcp.setup_server()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("server:app", host="0.0.0.0", port=8123, reload=True)