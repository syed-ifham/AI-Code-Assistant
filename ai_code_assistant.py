import openai
import os

# This project simulates a basic AI-powered code assistant using OpenAI's GPT API.
# NOTE: Set your OpenAI API key as an environment variable before running.

class AICodeAssistant:
    def __init__(self, model="gpt-3.5-turbo"):
        self.model = model
        self.api_key = os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError("Please set the OPENAI_API_KEY environment variable.")
        openai.api_key = self.api_key

    def generate_code(self, prompt: str, language: str = "python") -> str:
        """Generates code based on the user's prompt."""
        system_prompt = f"You are an expert {language} programmer. Generate clean, commented, professional {language} code."
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt},
            ],
            temperature=0.3,
            max_tokens=800
        )
        return response.choices[0].message['content']


def main():
    assistant = AICodeAssistant()
    print("AI Code Assistant Ready. Type your request (type 'exit' to quit).\n")
    while True:
        user_input = input("Prompt: ")
        if user_input.lower() == "exit":
            break
        lang = input("Language (default: python): ") or "python"
        try:
            result = assistant.generate_code(user_input, lang)
            print("\nGenerated Code:\n")
            print(result)
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
