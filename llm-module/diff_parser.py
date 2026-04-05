def clean_diff(diff_text: str) -> str:
    lines = diff_text.split("\n")
    useful_lines = []
    current_file = ""

    for line in lines:
        # Track file names for context
        if line.startswith("+++ b/"):
            current_file = line[6:]  # Extract file path
            useful_lines.append(f"File: {current_file}")
        elif line.startswith("+") or line.startswith("-"):
            # Exclude file headers and binary diffs
            if not line.startswith("+++ ") and not line.startswith("--- ") and not "@@" in line:
                useful_lines.append(line)
        # Optionally limit total lines to prevent overload
        if len(useful_lines) > 500:  # Arbitrary limit; adjust as needed
            useful_lines.append("[Diff truncated for brevity]")
            break

    return "\n".join(useful_lines)
