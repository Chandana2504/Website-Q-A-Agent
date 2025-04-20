# Website-Q-A-Agent
An AI agent that crawls help websites, understands their content, and answers user questions using Google Gemini model, Just enter a help URL, ask questions in natural language, and get accurate answers with source links!

# 🤖 Gemini-Powered Help Website Q&A Agent

This is an AI-powered question-answering agent that can crawl help websites (e.g., https://help.zluri.com), extract content, and accurately answer natural language questions about product features, integrations, and functionality using **Google Gemini 1.5 Flash** and **FAISS** for retrieval.

---

## 🧰 Features

✅ Accepts a help website URL as input  
✅ Crawls and processes all internal pages  
✅ Stores and indexes content using vector embeddings  
✅ Accepts natural language questions  
✅ Provides accurate answers with source links  
✅ Powered by Google Gemini 1.5 Flash for blazing fast responses  

---

## 🚀 Tech Stack

| Component | Library |
|----------|---------|
| Web Crawling | `requests`, `beautifulsoup4` |
| Environment Management | `python-dotenv` |
| Embeddings & LLM | `langchain`, `langchain_google_genai`, `google-generativeai` |
| Vector Store | `faiss-cpu` |
| Core Language | Python 3.9+ |

---

## 📦 Installation

### 1. Clone the repository
```bash
git clone https://github.com/your-username/qa-agent.git
cd qa-agent
2. Create a virtual environment (Windows)
cmd
Copy
Edit
python -m venv venv
venv\Scripts\activate
3. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
🔐 Add API Key
Create a file named .env in the root folder and paste:

ini
Copy
Edit
GOOGLE_API_KEY=your_gemini_api_key_here
🧪 Run the Agent
bash
Copy
Edit
python qa_agent.py --url https://help.zluri.com
