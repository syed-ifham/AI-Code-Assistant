# 🤖 AI Code Assistant

A command-line based AI code generator that uses OpenAI's GPT model to turn your natural language prompts into clean, professional, and commented code in various programming languages.

---

## 🔥 Features

- 🔎 Natural language to code generation
- 💬 Multi-language support (Python, Java, C++, etc.)
- 🧠 Clean and well-commented output
- 🔐 Secure API key usage (via environment variable)
- 🧱 Modular and professional Python structure

---

## 📦 Requirements

- Python 3.7+
- OpenAI Python SDK

Install dependencies:
```bash
pip install openai
```

---

## 🛠️ Setup

1. Clone the repository:
```bash
git clone https://github.com/your-username/ai-code-assistant.git
cd ai-code-assistant
```

2. Set your OpenAI API key:
```bash
export OPENAI_API_KEY=your-api-key-here  # Linux/macOS
# OR
set OPENAI_API_KEY=your-api-key-here     # Windows
```

3. Run the assistant:
```bash
python ai_code_assistant.py
```

---

## 🧪 Usage

```
Prompt: write a python function to reverse a string
Language (default: python): 
```
✅ Output:
```python
def reverse_string(s):
    # Reverses the input string and returns it
    return s[::-1]
```

---

## 💡 Example Prompts

| Prompt                              | Language |
|-------------------------------------|----------|
| "build a login form using tkinter"  | Python   |
| "bubble sort algorithm"             | Java     |
| "REST API with Flask"               | Python   |

---


---

## 🧠 Credits

Built with ❤️ by Ifham using OpenAI GPT technology.

---
