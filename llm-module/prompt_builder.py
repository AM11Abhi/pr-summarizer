def build_prompt(cleaned_diff: str) -> str:
    return f"""
You are a senior software engineer reviewing a pull request.

Summarize the following code changes in clear bullet points.

Focus on:
- features added
- bugs fixed
- refactoring
- improvements

Code changes:
{cleaned_diff}

Return only the summary.
"""