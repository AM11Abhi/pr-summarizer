# AI-Powered Pull Request Summarizer

This project aims to automate the generation of concise, human-readable summaries for GitHub Pull Requests using Large Language Models (LLMs) integrated through a CI/CD pipeline.

The system automatically analyzes code changes in a pull request and posts an AI-generated summary directly as a comment on the PR.

---

## 📌 Project Status

🚧 **In Progress**

- ✅ GitHub repository setup
- ✅ CI/CD automation using GitHub Actions (in progress)
- ⏳ LLM-based summarization module (to be integrated later)

> **Note:** The DevOps automation pipeline is being developed first.  
> The LLM logic will be integrated later without changing the CI/CD structure.

---

## ⚙️ How It Works (High-Level)

1. A Pull Request is opened or updated
2. GitHub Actions workflow is triggered
3. Repository is checked out with full history
4. Code changes are extracted using `git diff`
5. The diff is passed to a summarization module
6. A summary is posted as a comment on the Pull Request

---

## 🛠️ Technologies Used

- Git & GitHub
- GitHub Actions
- YAML
- Linux Shell Commands (`git diff`)
- GitHub REST API
- GitHub Secrets (for API keys)

---

## 🔀 Branching Strategy

- `main` – stable, reviewed code
- `feature/*` – development branches

All changes are merged into `main` via Pull Requests.

---

## 🎯 Objective

To build a **reliable, reusable GitHub Actions workflow** that automates pull request summarization and follows DevOps best practices such as:

- Event-based triggers
- Secure secret management
- Logging and observability
- Modular design

---

## 📈 Future Enhancements

- Integration with an LLM for real summaries
- Updating an existing PR comment instead of posting multiple comments
- Rate-limit handling and workflow optimization

---

