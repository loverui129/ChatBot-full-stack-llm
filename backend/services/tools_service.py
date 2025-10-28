from langchain.agents import Tool
from pydantic_core import Url
import requests
import os 
from dotenv import load_dotenv

load_dotenv()

# ====== rag tool=======
def rag_tool(question:str) -> str:  # use internal file(RAG) to answner questions
    from services.rag_service import query_rag
    return query_rag(question)

# =====weather tool======
def get_weather(city):
    try:
        api_key=os.getenv("WEATHER_API_KEY")
        if not api_key:
            return "❌ Weather API key not found. Please set WEATHER_API_KEY in your .env file."

        url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=no"
        res = requests.get(url, timeout=5).json()

        location = res.get("location", {}).get("name", city)
        current = res.get("current", {})
        temp = current.get("temp_c", "N/A")
        condition = current.get("condition", {}).get("text", "Unknown")
        humidity = current.get("humidity", "N/A")

        return f"Weather in {location}: {temp}°C, {condition}, humidity {humidity}%."

    except Exception as e:
        return f"Weather API error: {e}"

# ======stock API=======
def get_stock_price(symbol:str) ->str:
    try:
        import yfinance as yf
        ticker = yf.Ticker(symbol)
        price = ticker.history(period="1d")["Close"].iloc[-1]
        return f"{symbol.upper()} current price:${price:.2f}"
    except Exception as e:
        return f"stock API error :{e}"

# ====== Translator Tools ======
def translate_text(text: str) -> str:  # use Gpt to translate english <-> chinese
    try:
        from langchain_openai import ChatOpenAI
        llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.2)
        prompt = f"Translate the following text between English and Chinese, keeping the original meaning:\n\n{text}"
        result = llm.invoke(prompt)
        return f"🌐 Translation:\n{result.content}"
    except Exception as e:
        return f"Translation error: {e}"

# ====== Calculator Tools ======
def simple_calculator(expression: str) -> str:
    try:
        result = eval(expression, {"__builtins__": {}})
        return f"🧮 Result: {result}"
    except Exception as e:
        return f"Calculator error: {e}"


# ====== Websearch Tools ======
def web_search(query: str) -> str:  # use Serper.dev API to do web search
    try:
        api_key = os.getenv("SERPER_API_KEY")
        if not api_key:
            return "❌ SERPER_API_KEY not found. Please set it in .env."

        url = "https://google.serper.dev/search"
        payload = {"q": query}
        headers = {"X-API-KEY": api_key, "Content-Type": "application/json"}

        res = requests.post(url, headers=headers, json=payload, timeout=8).json()
        results = res.get("organic", [])[:3]

        if not results:
            return f"No web results for '{query}'."

        return "\n".join([f"🔗 {r['title']} — {r['link']}" for r in results])
    except Exception as e:
        return f"WebSearch error: {e}"

# ====== News Tools======
def get_news(topic: str) -> str: # get news title
    try:
        api_key = os.getenv("NEWS_API_KEY")
        if not api_key:
            return "❌ NEWS_API_KEY not found. Please set it in .env."

        url = f"https://newsapi.org/v2/everything?q={topic}&language=en&pageSize=3&apiKey={api_key}"
        res = requests.get(url, timeout=5).json()

        articles = res.get("articles", [])
        if not articles:
            return f"No news found for '{topic}'."

        headlines = [f"🗞 {a['title']}" for a in articles[:3]]
        return "\n".join(headlines)
    except Exception as e:
        return f"News API error: {e}"



# ====== register all tools====
def register_tools():
    return [
        Tool(name="RAGSearch", func=rag_tool,
             description="Answer questions using uploaded documents."),
        Tool(name="WeatherTool", func=get_weather,
             description="Get real-time weather information for a given city."),
        Tool(name="StockTool", func=get_stock_price,
             description="Get latest stock price for a given symbol (e.g., AAPL, TSLA)."),
        Tool(name="NewsTool", func=get_news,
             description="Fetch the latest news headlines about a given topic."),
        Tool(name="TranslateTool", func=translate_text,
             description="Translate text between English and Chinese."),
        Tool(name="CalculatorTool", func=simple_calculator,
             description="Perform simple arithmetic calculations."),
        Tool(name="WebSearchTool", func=web_search,
             description="Search the web for recent information using Serper.dev."),
    ]