from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq
from langchain.agents import initialize_agent
from tools import openalex_tool, idea_tool, gap_analysis_tool, phrase_extractor_tool

load_dotenv()

# Init LLM
llama_llm = ChatGroq(
    model="llama3-8b-8192",
    groq_api_key=os.getenv("GROQ_API_KEY"),
    temperature=0.7
)

# Register all tools
tools = [openalex_tool, idea_tool, gap_analysis_tool, phrase_extractor_tool]

agent_instructions = """
You are a formal, research-focused AI assistant.
Available tools:
1. OpenAlexPaperFetcher — fetches recent academic papers
2. ResearchIdeaGenerator — generates grounded research ideas from recent papers
3. ResearchGapAnalyzer — extracts trends and gaps from recent papers
4. KeyPhraseExtractor — extracts key terms and phrases from recent papers

Rules:
- If the user asks for research gaps, use ResearchGapAnalyzer.
- If the user asks for ideas/topics, use ResearchIdeaGenerator.
- If the user asks for key terms or vocabulary, use KeyPhraseExtractor.
- Always answer in a formal academic tone.
"""

agent = initialize_agent(
    tools,
    llama_llm,
    agent="zero-shot-react-description",
    verbose=True,
    handle_parsing_errors=True,
    agent_kwargs={"system_message": agent_instructions}
)

if __name__ == "__main__":
    print("Welcome to the AI Research Assistant Agent!")
    print("Examples:")
    print(" - 'Give me novel ideas in NLP'")
    print(" - 'Find research gaps in quantum computing'")
    print(" - 'Extract key phrases from hospital pharmacy research'")
    print(" - 'Fetch papers on reinforcement learning'")
    print("Type 'exit' to quit.\n")

    while True:
        query = input("Enter your query: ").strip()
        if query.lower() == "exit":
            print("Goodbye!")
            break
        response = agent.run(query)
        print("\n" + response + "\n")
