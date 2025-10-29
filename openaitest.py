# openaitest.py
# ------------------------------------------
# Test your OpenAI API connection and generate a short AI response
# ------------------------------------------

from openai import OpenAI
import os


# Make sure you've set your OpenAI API key:
# Windows: setx OPENAI_API_KEY "your-key-here"
# Mac/Linux: export OPENAI_API_KEY="your-key-here"

def main():

    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    try:
        # Test a simple prompt
        prompt = "Write a short introduction for an AI desktop assistant project."
        print("🔹 Sending request to OpenAI...")

        response = client.chat.completions.create(
            model="gpt-4o-mini",  # lightweight + fast; you can use 'gpt-4o' or 'gpt-3.5-turbo'
            messages=[
                {"role": "system", "content": "You are an AI assistant helping with a Python project."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=100
        )


        message = response.choices[0].message.content.strip()
        print("\n✅ OpenAI Response:\n")
        print(message)

    except Exception as e:
        print("\n❌ Error connecting to OpenAI API:")
        print(e)


if __name__ == "__main__":
    main()
