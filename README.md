# AI Agent Development Environment Setup

This guide provides a standardized workflow for setting up a Python environment tailored for building AI agents using LangChain, Google Gemini, and Ollama.

## 1. Project Initialization
```bash
# Initialize git (if not already done)
git init

# Create a .gitignore to protect secrets and environment files
echo .venv/ > .gitignore
echo .env >> .gitignore
echo __pycache__/ >> .gitignore
```

## 2. Environment Management
Use Python's built-in `venv` for lightweight isolation.

```powershell
# Create virtual environment
python -m venv .venv

# Activate (Windows PowerShell)
.\.venv\Scripts\Activate.ps1

# Activate (Windows Command Prompt)
.\.venv\Scripts\activate
```

## 3. Core Dependencies
Install the primary frameworks for orchestration and LLM connectivity.

```bash
# Update pip first
python -m pip install --upgrade pip

# Install essential libraries
pip install langchain langchain-google-genai langchain-ollama python-dotenv ipykernel

# Save for future use
pip freeze > requirements.txt
```

## 4. Configuration (.env)
Create a `.env` file in the root directory to store your API keys safely.

```env
# Google Gemini
GOOGLE_API_KEY=your_gemini_api_key_here

# Ollama (Defaults usually work, but can be customized)
OLLAMA_HOST=http://localhost:11434
```

## 5. Verification Script
Create a `test_env.py` to ensure both local and cloud LLMs are reachable.

```python
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_ollama import ChatOllama

load_dotenv()

def verify():
    # 1. Test Ollama (Assumes 'llama3' is pulled)
    try:
        local_llm = ChatOllama(model="llama3")
        print("✅ Ollama Local: ", local_llm.invoke("Hi").content)
    except Exception as e:
        print("❌ Ollama Error: ", e)

    # 2. Test Gemini
    try:
        cloud_llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")
        print("✅ Gemini Cloud: ", cloud_llm.invoke("Hi").content)
    except Exception as e:
        print("❌ Gemini Error: ", e)

if __name__ == "__main__":
    verify()
```

## 6. Recommended VS Code Extensions
- **Python**: IntelliSense, linting, and debugging.
- **Pylance**: High-performance language support.
- **Jupyter**: For running notebooks and interactive agent testing.
- **REST Client**: Useful for testing Ollama API endpoints directly.
