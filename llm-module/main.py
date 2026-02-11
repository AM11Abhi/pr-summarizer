import sys
from diff_parser import clean_diff


def main():
    if len(sys.argv) < 2:
        print("No diff file provided.")
        return

    diff_file = sys.argv[1]

    try:
        with open(diff_file, "r", encoding="utf-8") as f:
            diff_text = f.read()

        cleaned = clean_diff(diff_text)

        added = sum(1 for line in cleaned.split("\n") if line.startswith("+"))
        removed = sum(1 for line in cleaned.split("\n") if line.startswith("-"))

        print("## 🤖 Mock AI Summary")
        print(f"Total changes: {added + removed}")
        print(f"Lines added: {added}")
        print(f"Lines removed: {removed}")

    except Exception as e:
        print(f"Error processing diff: {e}")


if __name__ == "__main__":
    main()
