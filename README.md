# AI Incident Remediation System (LangGraph + Local LLMs)

An AI-powered incident analysis and remediation engine that processes infrastructure failure signals, diagnoses root causes, and generates actionable fixes such as Bash scripts and Terraform recommendations.

Built as a DevOps-focused system design project exploring AI automation, workflow orchestration, and local LLM integration.

---

## 🚀 Overview

This system simulates a real-world Site Reliability Engineering (SRE) workflow:

**Incident → Diagnosis → Remediation**

It ingests infrastructure incident logs and uses an LLM-powered LangGraph pipeline to:

* Analyze the issue
* Identify probable root cause
* Generate remediation steps
* Suggest infrastructure fixes (Terraform / Bash)

---

## 🧠 Architecture

```
Incident Input
      ↓
LangGraph Workflow Engine
      ↓
LLM (Ollama - Local Model)
      ↓
Diagnosis Node
      ↓
Remediation Node
      ↓
Structured Output (Fix Plan)
```

---

## ⚙️ Tech Stack

* Python
* LangGraph (workflow orchestration)
* Ollama (local LLM inference)
* PostgreSQL + pgvector (incident memory - in progress)
* Docker (containerized services)
* Nginx (reverse proxy / infra simulation)
* WSL2 Linux environment

---

## 📦 Features

* 🔍 Automated incident diagnosis from logs
* 🧠 LLM-powered root cause analysis
* 🛠️ Generates remediation steps (Bash / Terraform)
* 🧩 Modular LangGraph workflow design
* 🐳 Dockerized infrastructure components
* 📚 Ready for vector-based incident memory (pgvector integration)

---

## 🧪 Example Input

```
nginx returning 502 bad gateway
CPU usage at 95%
upstream connection timeout
```

## 📤 Example Output

* Root cause analysis
* Severity classification
* Suggested remediation actions:

  * Restart services
  * Scale upstream servers
  * Apply rate limiting
  * Infrastructure tuning recommendations

---

## 🏗️ Project Status

This project is currently in active development:

* [x] LangGraph workflow implemented
* [x] Local LLM integration (Ollama)
* [x] Basic incident → fix pipeline
* [x] Dockerized infrastructure components
* [ ] Structured JSON output system
* [ ] pgvector incident memory layer
* [ ] API layer (FastAPI)
* [ ] Production deployment (VPS / cloud)

---

## 🧠 Key Learnings

This project explores real-world challenges in building AI systems for infrastructure:

* Cloud IAM and permission failures
* Model runtime and compatibility issues
* Multi-step AI workflow reliability
* Debugging distributed AI pipelines
* Importance of deterministic outputs in automation systems

---

## ⚠️ Disclaimer

This system is for educational and experimental purposes.
Generated remediation steps should be reviewed before execution in production environments.

---

## 📌 Future Improvements

* Incident history + similarity search (pgvector)
* Slack / alerting integration
* GitHub Actions auto-remediation PRs
* Safe execution sandbox for fixes
* Multi-model routing (local + cloud LLMs)

---

## 👤 Author

Built as part of a DevOps + AI engineering learning journey.

---
