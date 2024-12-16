from crewai import Task
from Agents import *
from Tools import alat_cari
import os

def Pencarian_Data (input, sekolah):
    return Task(
    description=f"Cari lah berbagai informasi mengenai sekolah {sekolah} yang berkaita dengan pertanyaan = {input}",
    expected_output=f"List informasi tentang sekolah dan informasi untuk menjawab pertanyaan yang diberikan",
    agent= Pencari_Data,
    tools= None,
)

def Memberikan_jawaban(input): 
    return Task(
    description=f"jawablah pertanyaan pengguna = {input} berdasarkan data yang telah dicari dan cantumkan informasi terkait dalam bentuk link jika perlu",
    expected_output="untuk format saya sarankan kepadamu, buat lah format jawaban yang menarik dan membuat pembaca tertarik untuk mendapatkan informasi lebih lanjut",
    agent= Tour_guide,
    tools= alat_cari,
)