import openai
import os

class AICodeAssist:
    def __init__(self, model="gpt-3.5-turbo"):
        self.model = model
        self.api_key = os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError("Eroor set the OPENAI_API_KEY environment varable.")
        openai.api_key = self.api_key

    def generate_code(self, prompt: str, language: str = "python") -> str:
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
    assistant = AICodeAssist()
    print("BOOM! I am READY to go. Just Hit in Your request (or Type 'exit').\n")
    while True:
        user_input = input("Prompt: ")
        if user_input.lower() == "exit":
            break
        lang = input("Language (default: python): ") or "python"
        try:
            result = assistant.generate_code(user_input, lang)
            print("\nYour Code Sir/Madam:\n")
            print(result)
        except Exception as e:
            print(f"error: {e}")


if __name__ == "__main__":
    main()
