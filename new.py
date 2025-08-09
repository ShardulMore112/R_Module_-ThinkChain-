from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

llama_llm = ChatGroq(
    model="llama3-8b-8192",
    groq_api_key=os.getenv("GROQ_API_KEY"),
    temperature=0.7,
)

prompt = ChatPromptTemplate.from_template("""
You are an AI research advisor.
Suggest 3 innovative and feasible research topics in {field} for a {experience_level} researcher.
Maybe Tech Domain or May not be Tech Domain.
Include:
- a brief rationale for each topic
- all the skills and knowledge required to work on these topics
""")


chain = prompt | llama_llm

def recommended_topics(field: str, experience_level: str):
    response = chain.invoke({
        "field": field,
        "experience_level": experience_level
    })
    return response.content

if __name__ == "__main__":
    field = input("Enter the field of research: ")
    experience_level = input("Enter the experience level: ")
    topics = recommended_topics(field, experience_level)
    print(topics)
