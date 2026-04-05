# 🤖 AI-Powered Pull Request Summarizer

An automated GitHub Actions-based tool that generates **AI-powered summaries for Pull Requests** using Google Gemini.

---

## 🚀 Overview

This project integrates **GitHub Actions + Large Language Models (LLMs)** to automatically summarize pull requests.

Whenever a PR is created or updated:

* Code changes are extracted using `git diff`
* Changes are processed and sent to an AI model (Gemini)
* A concise summary is generated
* The summary is posted as a comment on the PR

---

## ⚙️ How It Works

```text
Pull Request Event
        ↓
GitHub Actions Workflow
        ↓
Extract Code Diff (git diff)
        ↓
Process Diff (cleaning)
        ↓
Send to Gemini AI
        ↓
Generate Summary
        ↓
Post Comment on PR
```

---

## 📁 Project Structure

```
pr-summarizer/
│
├── .github/
│   └── workflows/
│       └── pr-summary.yml      # GitHub Actions workflow
│
├── llm-module/
│   ├── main.py                # Main AI logic
│   └── diff_parser.py         # Diff cleaning utility
│
├── requirements.txt           # Dependencies
├── action.yml                 # Reusable GitHub Action definition
└── README.md
```

---

## 🔧 Setup & Usage

### For Your Own Repo (Reusable Action)

1. **Add the Action to Your Workflow**:
   Create `.github/workflows/pr-summarizer.yml` in your repo:

   ```yaml
   name: PR Summarizer
   on:
     pull_request:
       types: [opened, synchronize, reopened]
   jobs:
     summarize:
       runs-on: ubuntu-latest
       permissions:
         issues: write
         pull-requests: write
       steps:
         - uses: your-username/pr-summarizer@v1
           with:
             gemini_api_key: ${{ secrets.GEMINI_API_KEY }}
             base_ref: 'main'  # Optional: default 'main'
   ```

2. **Set Up Secrets**:
   - Go to your repo → Settings → Secrets → Actions
   - Add `GEMINI_API_KEY` with your Google Gemini API key

3. **Create a PR**: The action will automatically run and post a summary.

### Local Development

1. **Clone the Repository**

   ```bash
   git clone https://github.com/your-username/pr-summarizer.git
   cd pr-summarizer
   ```

2. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Test Locally**

   ```bash
   # Extract a diff (replace with actual commands)
   git diff HEAD~1 > test_diff.txt
   # Run the summarizer
   GEMINI_API_KEY=your_key python llm-module/main.py test_diff.txt
   ```

---

## 🧪 Example Output

```
🤖 AI Pull Request Summary

Key Changes
• Added invoice calculation functions
• Implemented discount logic with validation
• Improved code structure

Impact
Enhances functionality by introducing structured business logic and improving maintainability.
```

---

## 🔑 Key Features

* ✅ Automatic PR summarization
* ✅ GitHub Actions integration
* ✅ Uses Google Gemini (LLM)
* ✅ Clean diff processing
* ✅ Fully automated commenting
* ✅ Works on every PR update
* ✅ Configurable inputs (base branch, model, etc.)
* ✅ Error handling for edge cases

---

## ⚠️ Limitations

* 🔒 External contributors (fork PRs) cannot access API keys
* 📏 Large PRs are truncated (future improvement: chunking)
* 🤖 AI summaries may not always be perfect

---

## 🚀 Future Improvements

* Risk level detection (Low / Medium / High)
* AI code review suggestions
* Chunking for large diffs
* Update existing comment instead of creating new ones
* Convert into reusable GitHub Action (Marketplace)

---

## 🧠 Tech Stack

* Git & GitHub
* GitHub Actions (CI/CD)
* Python
* Google Gemini API
* YAML

---

## 📌 Key Concept

> This project demonstrates how AI can be integrated into DevOps pipelines to automate code review assistance.

---

