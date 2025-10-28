from langchain.agents import create_react_agent, AgentExecutor
from langchain import hub
from langchain_openai import ChatOpenAI
from services.tools_service import register_tools
import os
from dotenv import load_dotenv

# load 
load_dotenv()

# Initialize LLM
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.4,
    api_key=os.getenv("OPENAI_API_KEY")
)

# register all tools
tools = register_tools()

# Initialize LangChain Agent
prompt = hub.pull("hwchase17/react")
agent = create_react_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)


# unified interface
def run_agent(query: str) -> str: # accept NLP-> The agent automatically determines and calls the appropriate tool
    
    try:
        result = agent_executor.invoke({"input": query})
        return result["output"]
    except Exception as e:
        return f"❌ Agent error: {e}"
