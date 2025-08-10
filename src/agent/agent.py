from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq
from langchain.agents import initialize_agent
from tools import openalex_tool, idea_tool, gap_analysis_tool, phrase_extractor_tool

load_dotenv()


llama_llm = ChatGroq(
    model="llama3-8b-8192",
    groq_api_key=os.getenv("GROQ_API_KEY"),
    temperature=0.7
)


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
    
    domain_name = input("Enter the research domain: ").strip()
    experience_level = input("Enter the experience level (e.g., expert, intermediate, beginner): ").strip()
    
    query = f"""Fetch Recent Papers on Openalex about {domain_name}, find research gaps in the current workflow and generate novel research ideas for a {experience_level} researcher
            The  output should have the following format:
                1. Novel Research Idea 1(Title):
                   1.2 description abbout the ideas:Description about the idea
                   1.3 skills required: enlisted skills required
                2. Novel Research Idea 2(Title):
                     2.2 description about the ideas:Description about the idea
                     2.3 skills required:enlisted skills required
                3. Novel Research Idea 3(Title):
                     3.2 description about the ideas:Description about the idea
                     3.3 skills required:enlisted skills required


                Research Gaps:
                1. Gap 1
                2. Gap 2
                3. Gap 3
                """
    
    
    try:
        response = agent.run(query)
        print("\n" + response + "\n")
    except Exception as e:
        print(f"Error during agent execution: {e}")