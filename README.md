# 🛡️ Log Redactor

[![Python Version](https://img.shields.io/badge/python-3.9%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code Style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![CI](https://img.shields.io/badge/build-passing-brightgreen.svg)]()

**Log Redactor** is a high-performance CLI tool and library designed to identify and mask Personally Identifiable Information (PII) within application logs and text streams. It serves as a critical security layer, ensuring data privacy compliance by scrubbing credentials, emails, and personal identifiers before logs are transmitted to external monitoring platforms like Datadog, Splunk, or ELK.

---

## 🚩 Problem Statement

In modern distributed systems, developers frequently leak sensitive data—such as authentication tokens, credit card numbers, and personal emails—into application logs. This creates significant security vulnerabilities and risks violating strict data privacy regulations like **GDPR**, **CCPA**, and **PCI-DSS**. Manual log auditing is impossible at scale; **Log Redactor** automates this process with minimal latency.

### Target Audience
- **DevSecOps Engineers** looking to automate log sanitization.
- **Backend Developers** needing to scrub PII before local or remote logging.
- **Compliance Officers** ensuring data residency and privacy standards.

---

## ✨ Key Features

- **Pattern-Based Redaction:** Out-of-the-box support for common sensitive data types including IPv4/v6 addresses, Emails, Credit Cards, and JWTs.
- **JSON-Aware Scrubbing:** Intelligently targets specific JSON keys (e.g., `password`, `secret_key`) while preserving the overall structure and validity of the log entry.
- **Stream Processing:** Optimized for high-throughput, handling multi-gigabyte log files with minimal memory overhead using buffer-based processing.
- **YAML-Based Configuration:** Fully customizable redaction rules and project-specific exclusion lists defined via a simple `config.yaml`.

---

## 🏗️ Architecture & System Design

The system is built with a modular approach to separate the redaction logic from the interface (CLI/API).

| Module | Purpose |
| :--- | :--- |
| `src/models.py` | Pydantic domain models for redaction requests, rule definitions, and response schemas. |
| `src/config.py` | YAML configuration loader, regex pattern compiler, and exclusion rule parser. |
| `src/core.py` | The engine: handles regex matching, JSON key scrubbing, and streaming buffer logic. |
| `src/api.py` | FastAPI HTTP routes and streaming endpoint handlers for server-mode deployment. |
| `src/cli.py` | Command-line argument processing and stdin/file stream piping orchestrator. |
| `src/main.py` | Application entrypoint launching either the CLI tool or Uvicorn Web Server. |

---

## 🛠️ Technology Stack

- **Language:** [Python 3.9+](https://www.python.org/)
- **CLI Framework:** [Typer](https://typer.tiangolo.com/) (Fast and intuitive CLI)
- **Data Validation:** [Pydantic](https://docs.pydantic.dev/) (Strict schema enforcement)
- **Configuration:** [PyYAML](https://pyyaml.org/)
- **UI/Formatting:** [Rich](https://rich.readthedocs.io/) (Beautiful terminal output)
- **Testing:** [pytest](https://docs.pytest.org/)
- **Web Framework:** [FastAPI](https://fastapi.tiangolo.com/) (For API-based redaction)

---

## 🚀 Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/your-org/log-redactor.git
cd log-redactor
```

### 2. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

---

## ⚙️ Environment Variables Configuration

Create a `.env` file in the root directory based on `.env.example`:

```env
LOG_LEVEL=INFO
APP_MODE=CLI  # Options: CLI, SERVER
API_HOST=0.0.0.0
API_PORT=8000
CONFIG_PATH=config.yaml
```

---

## 📖 Usage

### CLI Mode
Redact a single string or a file directly from your terminal.

**Redact a string:**
```bash
python src/main.py redact "User login failed for email: admin@example.com from IP: 192.168.1.1"
```

**Stream a log file:**
```bash
cat access.log | python src/main.py stream
```

### API Mode
Start the redaction server to handle requests over HTTP.

**Start Server:**
```bash
python src/main.py start-server
```

**Request Example:**
```bash
curl -X 'POST' 'http://localhost:8000/redact' \
  -H 'Content-Type: application/json' \
  -d '{"text": "My secret token is eyJhbGciOiJIUzI1Ni..."}'
```

---

## 🧪 Automated Testing

We use `pytest` to ensure the redaction engine and API endpoints remain robust.

**Run all tests:**
```bash
pytest
```

**Run specific test suites:**
```bash
pytest tests/test_core.py  # Test redaction logic
pytest tests/test_api.py   # Test HTTP endpoints
```

---

## 📂 Project Structure

```text
.
├── src/
│   ├── __init__.py
│   ├── api.py          # FastAPI routes
│   ├── cli.py          # Typer CLI commands
│   ├── config.py       # YAML/Regex configuration
│   ├── core.py         # Redaction engine
│   ├── main.py         # App entrypoint
│   └── models.py       # Pydantic schemas
├── tests/
│   ├── __init__.py
│   ├── test_api.py     # API integration tests
│   └── test_core.py    # Unit tests for redaction
├── .env.example        # Template for env vars
├── .gitignore
├── config.yaml         # Redaction rules definition
├── requirements.txt    # Project dependencies
└── README.md           # Documentation
```

---

## 🗺️ Roadmap

- [ ] **Dockerization:** Provide a lightweight Docker image for sidecar deployments.
- [ ] **Presidio Integration:** Optional integration with Microsoft Presidio for NLP-based PII detection.
- [ ] **Custom Masking Styles:** Support for partial masking (e.g., `****-****-****-1234`).
- [ ] **Performance Benchmarking:** Automated scripts to measure throughput (GB/s).

---

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

---

**Daily Project Factory** - *Engineering Excellence, One Project at a Time.*