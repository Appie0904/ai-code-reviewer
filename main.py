import openai
import streamlit as st


openai.api_key = "your_openai_api_key"  # Replace with your OpenAI API key

def analyze_code(code_snippet):
    prompt = f"Review this Python code and suggest improvements:\n\n{code_snippet}\n\nSuggestions:"
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "You are an AI code reviewer."},
                  {"role": "user", "content": prompt}]
    )
    
    return response["choices"][0]["message"]["content"]



st.title("AI Code Reviewer")
code_input = st.text_area("Enter your Python code:")
if st.button("Analyze Code"):
    suggestions = analyze_code(code_input)  # Calls the OpenAI API
    st.write(suggestions)



# Example usage
code = """
def add_numbers(a, b):
    sum = a + b
    return sum
"""
print(analyze_code(code))
