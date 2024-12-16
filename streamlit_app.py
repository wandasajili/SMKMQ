import streamlit as st
from crewai import Crew, Process  
from Agents import *  
from Tasks import * 
import os

# Menambahkan logo

st.set_page_config(page_title="SMK MADINATUL QUR'AN", page_icon="logo/logo_MQ.png", layout="wide")

# sidebar

# st.sidebar.image("logo/baner.jpg", width=400) 
st.image("logo/logo_MQ.png", width=120) 

# jangan di apaapain
st.title("MQ.AI")
sekolah = st.text_input("Nama Sekolah?")
pertanyaan = st.text_input("Silahkan masukan pertanyaan anda!")
submit = st.button("Submit")

Crew_instance = Crew (
  agents=[Pencari_Data, Tour_guide],
  tasks=[Pencarian_Data(pertanyaan, sekolah), Memberikan_jawaban(pertanyaan)],
  manager_llm=llm,
  Process=Process.sequential
)

if submit and sekolah and pertanyaan:
 st.markdown(Crew_instance.kickoff())