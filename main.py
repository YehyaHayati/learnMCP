from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent
import asyncio
from dotenv import load_dotenv
load_dotenv()

client = MultiServerMCPClient({
    # "Stock_Search": {
    #     "transport":"streamable_http",
    #     "url":"http://localhost:8000/mcp/"
    # },
    "Github": {
        "transport": "streamable_http",
        "url": "https://api.githubcopilot.com/mcp/"
    }
    # "Calculator": {
    #     "transport":"streamable_http",
    #     "url":"http://localhost:8001/mcp/"
    # }
})

async def main():
    tools = await client.get_tools()
    agent = create_react_agent(model=ChatOpenAI(), tools=tools, verbose=True)
    # question = "What is the stock of AAPL, tell me all of the information, and calculate the difference between High and Low."
    question = "Get me the readme of the repo MohammadYehya/GridForge."
    print(question)
    res = await agent.ainvoke({"messages":question})
    # for r in res['messages']:
    #     print("_"*50)
    #     print(r)
    print(res['messages'][-1].content)
    

asyncio.run(main())