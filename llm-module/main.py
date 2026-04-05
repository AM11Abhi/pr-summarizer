import sys
import os
from google import genai

# Add the script's directory to the path so diff_parser can be imported
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from diff_parser import clean_diff

def main():
    if len(sys.argv) < 2:
        print("Error: No diff file provided.")
        sys.exit(1)

    diff_file = sys.argv[1]
    api_key = os.getenv('GEMINI_API_KEY')
    model = os.getenv('MODEL', 'gemini-2.5-flash')

    if not api_key:
        print("Error: GEMINI_API_KEY not set.")
        sys.exit(1)

    try:
        with open(diff_file, "r", encoding="utf-8", errors='ignore') as f:
            diff_text = f.read()

        if not diff_text.strip():
            print("## 🤖 AI Pull Request Summary\n\nNo changes detected in the diff.")
            return

        cleaned_diff = clean_diff(diff_text)
        max_chars = int(os.getenv('MAX_DIFF_CHARS', '6000'))
        cleaned_diff = cleaned_diff[:max_chars]

        client = genai.Client(api_key=api_key)

        prompt = f"""
You are an AI assistant that summarizes GitHub pull requests.

Create a short summary using this format:

## 🤖 AI Pull Request Summary

Key Changes
- bullet points of major changes

Impact
- one or two sentences describing the purpose

Keep the response concise (max 120 words).

Code changes:
{cleaned_diff}
"""

        response = client.models.generate_content(
            model=model,
            contents=prompt
        )

        if response and response.text:
            print(response.text)
        else:
            print("## 🤖 AI Pull Request Summary\n\nSummary generation failed—please check the diff or API key.")

    except Exception as e:
        print(f"## 🤖 AI Pull Request Summary\n\nError generating summary: {str(e)}")

if __name__ == "__main__":
    main()