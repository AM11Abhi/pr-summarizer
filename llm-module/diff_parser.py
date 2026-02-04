def clean_diff(diff_text: str) -> str:
    lines = diff_text.split("\n")
    useful_lines = []

    for line in lines:
        if line.startswith("+") or line.startswith("-"):
            if not line.startswith("+++ ") and not line.startswith("--- "):
                useful_lines.append(line)

    return "\n".join(useful_lines)
