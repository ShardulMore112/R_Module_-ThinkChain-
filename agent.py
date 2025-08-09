from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq
from langchain.agents import initialize_agent
from tools import openalex_tool  # Your paper fetch tool

load_dotenv()

llama_llm = ChatGroq(
    model="llama3-8b-8192",
    groq_api_key=os.getenv("GROQ_API_KEY"),
    temperature=0.7,
)

tools = [openalex_tool]

agent = initialize_agent(
    tools,
    llama_llm,
    agent="zero-shot-react-description",
    verbose=True,
)

if __name__ == "__main__":
    print("Welcome to the AI Research Assistant Agent!")
    print("You can ask for research topics or ask to fetch papers.")
    print("Type 'exit' to quit.\n")
    
    while True:
        query = input("Enter your query: ").strip()
        if query.lower() == "exit":
            print("Goodbye!")
            break
        response = agent.run(query)
        print("\n" + response + "\n")
