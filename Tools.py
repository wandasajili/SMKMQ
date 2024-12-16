import os
from dotenv import load_dotenv
from langchain_community.tools import TavilySearchResults

load_dotenv()
os.environ["TAVILY_API_KEY"] = os.getenv("tavilyapi-key")
alat_cari =[TavilySearchResults(k=5)]
