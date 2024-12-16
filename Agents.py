from crewai import Agent
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

llm = ChatOpenAI(
    openai_api_base="https://api.groq.com/openai/v1",
    openai_api_key=os.environ['GROQ_API_KEY'],
    model_name="groq/llama3-8b-8192",
    temperature=0,
    max_tokens=1000,
)


Pencari_Data = Agent(
    role="Pencarian_Data",
    goal="mencari data secara online mengenal sekolah untuk menjawab pertanyaan pengguna",
    backstory="kamu adalah staff tata usaha di sekolah kamu memiliki wawasan yang lengkap tentang sekolah kamu bekerja",
    allow_delegation=False,
    verbose=True,
    llm = llm,
)

Tour_guide = Agent(
    role="Tour guide sekolah",
    goal="Memberikan berbagai informasi terkait sekolah untuk menjawab pertanyaan pengunjung",
    backstory="kamu adalah seorang tata usaha di suatu sekolah yang bekerja secara khusus untuk menjadi tour guide peengunjung sekolah dan menjawab pertanyaan mereka seputar sekolah",
    allow_delegation=False,
    verbose=True,
    llm = llm,  
)


