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
└── README.md
```

---

## 🔧 Setup & Usage

### For This Repository

#### 1️⃣ Clone the Repository

```bash
git clone https://github.com/AM11Abhi/pr-summarizer.git
cd pr-summarizer
```

#### 2️⃣ Add API Key (Important)

Go to:

```
Repo → Settings → Secrets → Actions
```

Add:

```
GEMINI_API_KEY = your_api_key
```

#### 3️⃣ Create a Pull Request

* Create a new branch
* Make code changes
* Open a PR to `main`

👉 The workflow will automatically run and post a summary.

### Using This Action in Your Own Repository

You can use this action in any GitHub repository by adding a workflow file:

#### 1️⃣ Create Workflow File

Create `.github/workflows/pr-summary.yml` in your repository:

```yaml
name: PR Summary

on:
  pull_request:
    types: [opened, synchronize, reopened]

permissions:
  contents: read
  pull-requests: write

jobs:
  summarize:
    runs-on: ubuntu-latest
    steps:
      - name: Summarize PR
        uses: AM11Abhi/pr-summarizer@v1.0.0
        with:
          gemini_api_key: ${{ secrets.GEMINI_API_KEY }}
```

#### 2️⃣ Add API Key Secret

In your repository settings:

```
Settings → Secrets → Actions → New repository secret
```

Name: `GEMINI_API_KEY`
Value: Your Google Gemini API key

#### 3️⃣ Test It

Create a PR in your repository - the action will automatically summarize it!

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

