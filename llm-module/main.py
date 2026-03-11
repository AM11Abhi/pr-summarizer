import sys
from diff_parser import clean_diff
from prompt_builder import build_prompt
from local_llm  import generate_summary


def main():

    if len(sys.argv) < 2:
        print("No diff file provided.")
        return

    diff_file = sys.argv[1]

    try:
        with open(diff_file, "r", encoding="utf-8") as f:
            diff_text = f.read()

        cleaned = clean_diff(diff_text)

        # Build prompt
        prompt = build_prompt(cleaned)

        # Send to local LLM
        summary = generate_summary(prompt)

        print("## 🤖 AI PR Summary\n")
        print(summary)

    except Exception as e:
        print(f"Error processing diff: {e}")


if __name__ == "__main__":
    main()