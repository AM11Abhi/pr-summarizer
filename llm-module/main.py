import sys
import os
import google.generativeai as genai
from diff_parser import clean_diff

def main():
    if len(sys.argv) < 2:
        print("No diff file provided.")
        return

    diff_file = sys.argv[1]

    try:
        with open(diff_file, "r", encoding="utf-8") as f:
            diff_text = f.read()

        cleaned_diff = clean_diff(diff_text)

        # Limit size to avoid huge prompts
        cleaned_diff = cleaned_diff[:6000]

        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            print("GEMINI_API_KEY not set")
            return

        genai.configure(api_key=api_key)

        model = genai.GenerativeModel("gemini-1.5-flash-latest")

        prompt = f"""
You are an AI code reviewer.

Summarize the following pull request changes.

Explain:
- What changed
- Key improvements
- Possible purpose of the changes

Code changes:
{cleaned_diff}
"""

        response = model.generate_content(prompt)

        print("## 🤖 AI Pull Request Summary\n")
        print(response.text)

    except Exception as e:
        print(f"Error generating summary: {e}")

if __name__ == "__main__":
    main()