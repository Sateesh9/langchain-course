from langchain_tavily import TavilySearch
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

tavily = TavilySearch()
@tool
def weather_tool(city: str) -> dict:
    """A tool that returns the current weather."""
    return tavily.invoke({"query": f"current weather in {city}"})

llm = ChatOpenAI(model="gpt-6-luna", temperature=1)
tools = [TavilySearch()]
agent = create_agent(model=llm, tools=tools)



def main():
    agentM= agent.invoke({"messages" :[HumanMessage(content="What is the weather in New York?")]
        })
    print(agentM)


if __name__ == "__main__":
    main()
