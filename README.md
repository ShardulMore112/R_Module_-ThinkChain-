# 📚 AI Research Assistant Agent — ##THINKCHAIN##

## 📌 Overview
The **AI Research Assistant Agent** is part of *The_R_Module* and is designed to assist researchers in:
- Fetching **recent academic papers** from OpenAlex
- Identifying **research gaps** & underexplored areas
- Suggesting **novel, feasible research ideas**
- Extracting **key technical terms and phrases**

It leverages **LangChain**, **Groq LLaMA 3 models**, and custom analysis tools to produce **formal, academic-style outputs** tailored to a user's research experience level.

This tool is ideal for students, academics, and research professionals who want **informed, data-backed AI assistance** for brainstorming and literature review.

---

## 🚀 Features
- **Groq LLaMA 3-powered AI agent** with a formal academic personality
- **Four Integrated Tools**:
  1. **OpenAlexPaperFetcher** – Fetches recent papers relevant to a topic
  2. **ResearchIdeaGenerator** – Generates grounded research ideas with rationale & required skills
  3. **ResearchGapAnalyzer** – Identifies major trends and research gaps
  4. **KeyPhraseExtractor** – Extracts key phrases and terms from papers
- Automatic **paper fetching + AI analysis** workflow
- Modular tool design for future extensions
- Simple interactive CLI interface

---


## 🔧 Installation
1. **Clone the repository**
git clone https://github.com/ShardulMore112/The_R_Module.git
cd The_R_Module/src/agent


2. **Create a virtual environment** (recommended)
python -m venv venv
source venv/bin/activate # macOS/Linux
venv\Scripts\activate # Windows


3. **Install dependencies**
pip install -r requirements.txt


4. **Set environment variables**
Create a `.env` file inside `src/agent`:
GROQ_API_KEY=your_groq_api_key_here


## ▶️ Usage
Run the interactive agent:
python agent.py


You will be prompted for:
1. **Research domain** (e.g., "Quantum Computing", "Reinforcement Learning")
2. **Your experience level** (expert, intermediate, beginner)

The agent will:
- Fetch top papers from OpenAlex
- Identify research gaps
- Propose structured research ideas
- Output key findings in **academic format**

**Example:**
Welcome to the AI Research Assistant Agent!
Enter the research domain: Large Language Models
Enter the experience level: intermediate
...
[Generated research ideas, trends, and gaps]


---

## 🛠 How It Works

### 1. **Language Model Backend**
- Uses **Groq LLaMA 3 (llama3-8b-8192)** for high-speed, context-rich responses
- Formal tone enforced through `system_message` prompts

### 2. **Tools**
Defined in `tools.py` using LangChain's `Tool` API:

| Tool Name | Function | Description |
|-----------|----------|-------------|
| OpenAlexPaperFetcher | `fetch_openalex_papers()` | Fetches top recent papers |
| ResearchIdeaGenerator | `generate_ideas_with_papers()` | Suggests innovative ideas |
| ResearchGapAnalyzer  | `analyze_research_gaps()` | Finds gaps & emerging trends |
| KeyPhraseExtractor   | `extract_key_phrases()` | Extracts key research terms |

### 3. **OpenAlex API**
- Queries academic papers based on topic & relevance
- Reconstructs abstracts from inverted index format
- Outputs paper metadata including title, authors, and year

---

## 📄 Example Outputs

### **Research Idea Example**
1.Adaptive Curriculum Learning in LLM Fine-tuning

1.2 Description: Investigates progressive task difficulty adjustments during fine-tuning of LLMs for domain-specific knowledge acquisition.

1.3 Skills Required: NLP, Reinforcement Learning, PyTorch, Prompt Engineering


### **Research Gaps Example**
Research Gaps:
Lack of interpretability in reasoning chains for large-scale models.

Underexplored cross-lingual benchmarking for LLMs.

Absence of datasets for low-resource academic domains.

## 📬 Contact
**Author:** Shardul More 
📧 Email: [shardulmoreofficial@gmail.com](mailto:shardulmoreofficial@gmail.com)    
B.Tech in CSE (AI/ML) — Rajarambapu Institute of Technology, Islampur  
Passionate about **NLP, LLMs, AI-powered research tools, and formal mathematics**  
Interested in AI research towards innovative publications
