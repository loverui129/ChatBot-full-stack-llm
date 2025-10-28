from langchain.agents import initialize_agent
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
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent_type="zero-shot-react-description",  # auto chosse right tools    
    verbose=True  # output logs
)

# unified interface
def run_agent(query: str) -> str: # accept NLP-> The agent automatically determines and calls the appropriate tool
    
    try:
        result = agent.run(query)
        return result
    except Exception as e:
        return f"❌ Agent error: {e}"
