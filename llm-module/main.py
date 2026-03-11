import sys
import os
from google import genai
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

        # limit prompt size
        cleaned_diff = cleaned_diff[:6000]

        # initialize Gemini client
        client = genai.Client()

        prompt = f"""
You are an AI code reviewer.

Summarize the following pull request changes.

Explain:
- What changed
- Key improvements
- Purpose of the changes

Code changes:
{cleaned_diff}
"""

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        print("## 🤖 AI Pull Request Summary\n")
        print(response.text)

    except Exception as e:
        print(f"Error generating summary: {e}")


if __name__ == "__main__":
    main()