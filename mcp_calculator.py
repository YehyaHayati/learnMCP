from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Calculator", port=8001)

@mcp.tool()
def add(a: float, b: float) -> float:
    """Adds 2 numbers and returns their sum."""
    return a + b
@mcp.tool()
def dif(a: float, b: float) -> float:
    """Subtracts 2 numbers and returns their difference."""
    return a - b
@mcp.tool()
def mul(a: float, b: float) -> float:
    """Multiplies 2 numbers and returns their product."""
    return a * b
@mcp.tool()
def div(a: float, b: float) -> float:
    """Divides 2 numbers and returns their result."""
    return a / b

mcp.run(transport="streamable-http")