from mcp.server.fastmcp import FastMCP
import requests

mcp = FastMCP("Stock_Search")

@mcp.tool()
async def main(symbol:str):
    """Takes a symbol of a stock and searches for it using the API."""
    # response = requests.get(f"https://api.polygon.io/v1/open-close/{symbol}/2025-08-05?adjusted=true&apiKey=YKy_XtiZCuQAxnYOnZgpagdF0TlEgMtb")
    # print(response.json())
    # return response.json()

    return {
        "status": "OK",
        "from": "2025-08-06",
        "symbol": "AAPL",
        "open": 205.63,
        "high": 215.38,
        "low": 205.59,
        "close": 213.25,
        "volume": 108483103,
        "afterHours": 219.26,
        "preMarket": 203.33
        }


mcp.run(transport="streamable-http")