# Kube-SRE-Vantage 🚀
**AI-Powered Infrastructure Reliability Framework for Managed Kubernetes**

Kube-SRE-Vantage is a Python-based framework designed to automate the lifecycle of Production Engineering at scale. It bridges the gap between raw telemetry and actionable intelligence by integrating **OpenTelemetry (OTel)** with **Generative AI (LLMs/SLMs)** to manage SRE KPIs across AKS, EKS, and GKE.

---

## 🌟 Key Features

### 🧠 Vantage AI Engine
- **LLM-Powered Root Cause Analysis (RCA):** Automatically analyzes "Trace Deltas" using LLMs (Llama 3, GPT-4, etc.) to diagnose SLO breaches in seconds.
- **Edge SLM Log Diagnostics:** Utilizes Small Language Models (SLMs) to detect pre-failure signatures in high-volume Kubernetes events and node-level logs.
- **GenAI Remediation Playbooks:** Generates context-aware repair instructions and automates "drains" or "restarts" with high-confidence AI verification.

### 📊 Standardized Observability (OTel)
- **Vendor-Neutral Telemetry:** Uses OpenTelemetry to unify metrics, logs, and traces across diverse cloud providers (AWS, Azure, GCP).
- **Hardware-Aware Insights:** Standardizes data from cloud-managed hardware (e.g., AWS Nitro, Azure Boost) into a unified SRE dashboard.

### 🛡️ SRE KPI Enforcement
- **Automated SLO Management:** Real-time tracking of Availability and Latency targets.
- **Error Budget Guardrails:** Implements automated "Stop-Ship" signals and deployment blocks based on remaining error budgets.
- **MTTR Reduction:** Dramatically lowers Mean Time to Repair through automated diagnosis and suggested remediation.

---

## 🏗️ Technical Architecture

### 1. Telemetry Layer (Python SDK)
Ingests data using the `opentelemetry-sdk`, providing a consistent interface for multi-cloud environments.

### 2. Intelligence Layer (LiteLLM)
Uses `litellm` to interface with various AI providers, enabling the framework to switch between LLMs for complex RCA and SLMs for edge-based log analysis.

### 3. Kubernetes Controller (Kopf)
A Python-based operator framework that translates AI insights into cluster actions (e.g., scaling, draining, or self-healing).

---

## 📂 Project Structure

```text
kube-sre-vantage/
├── agents/
│   ├── rca_agent.py          # LLM Logic for Root Cause Analysis
│   └── health_monitor.py     # OTel Metric & Trace processor
├── controllers/
│   ├── slo_controller.py     # K8s Operator for SLO enforcement
│   └── remediation_ops.py    # Automated actions (drain, scale, restart)
├── api/v1/                   # REST API for SRE Dashboard
├── config/
│   ├── slos.yaml             # SLO & Alerting thresholds
│   └── otel_config.yaml      # OTel Collector configuration
└── main.py                   # Framework entry point
```

---

## ☁️ Cloud Agnostic Support
- **AWS EKS:** Integrated with AWS Distro for OpenTelemetry (ADOT).
- **Azure AKS:** Native support for Azure Monitor & Managed Grafana.
- **Google GKE:** Seamless connection to Google Cloud Operations Suite.

---

## 🚀 Getting Started

1. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
2. **Configure SLOs:** Define your targets in `config/slos.yaml`.
3. **Run the Framework:**
   ```bash
   python main.py
   ```

---

## 🤝 Production Engineering Philosophy
Kube-SRE-Vantage is built on the belief that at modern scale, **observability is not enough—understanding is required**. By leveraging GenAI to parse the complex relationship between infrastructure and applications, we reduce the cognitive load on SRE teams and move from reactive alerting to proactive reliability.
