# AI Code Reviewer 🤖

An AI-powered tool that analyzes Python code and provides suggestions for improvements using OpenAI’s GPT-4.

🚀 Features

✅ Reviews Python code for best practices
✅ Detects naming issues, optimization opportunities, and errors
✅ Provides AI-generated suggestions to improve code quality

📌 Installation

1️⃣ Clone the repository

git clone https://github.com/your-username/ai-code-reviewer.git
cd ai-code-reviewer

2️⃣ Install dependencies

pip install openai

🔑 Setup
	1.	Get an OpenAI API key from OpenAI.
	2.	Replace "your_openai_api_key" in the script with your actual API key.

📝 Usage

Run the script with your Python code snippet:

import openai

openai.api_key = "your_openai_api_key"  # Replace with your OpenAI API key

def analyze_code(code_snippet):
    prompt = f"Review this Python code and suggest improvements:\n\n{code_snippet}\n\nSuggestions:"
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "You are an AI code reviewer."},
                  {"role": "user", "content": prompt}]
    )
    
    return response["choices"][0]["message"]["content"]

# Example usage
code = """
def add_numbers(a, b):
    sum = a + b
    return sum
"""
print(analyze_code(code))

🎯 Example Output

1. Consider renaming 'sum' to avoid conflict with the built-in 'sum' function.
2. Add type hints: def add_numbers(a: int, b: int) -> int:
3. Include a docstring to explain the function's purpose.

💡 Next Steps

🚀 Expand this project by adding:
	•	More AI-powered checks (security flaws, complexity analysis)
	•	A web interface using Streamlit
	•	GitHub Actions integration for automatic PR reviews

🛠️ Contributions

Feel free to fork this project and submit PRs!
If you have ideas, open an issue 🚀

📜 License

MIT License © 2024

✨ Happy Coding! 🚀
