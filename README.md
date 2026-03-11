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

## 🔍 How it Works: The SRE Vantage Loop

Kube-SRE-Vantage follows a **closed-loop reliability cycle** powered by data and context:

### 1. Ingestion (OpenTelemetry)
The framework continuously ingests Service Level Indicators (SLIs) like success rates, error counts, and latency through standard **OpenTelemetry** protocols. This ensures that no matter where the service is running (EKS, AKS, GKE), the telemetry is normalized.

### 2. Contextualization (RAG Agent)
When the framework evaluates a service, it doesn't just look at the numbers. The **RAG (Retrieval-Augmented Generation) Agent** pulls context from a vector database (ChromaDB) containing:
- **Historical Incidents:** Past post-mortems and root causes.
- **SLA Documentation:** Specific contractual uptime commitments.
- **Service Mesh Topography:** Knowledge of upstream/downstream dependencies.

### 3. Analysis (SLO Engine)
The **SLO Engine** takes the normalized SLIs from OTel, the service definitions from **OpenSLO**, and the retrieved context from the RAG Agent. It feeds this into an LLM (via LiteLLM) to perform an intelligent health check:
- **Health Calculation:** Compares current SLIs against SLO targets.
- **Burn Rate Prediction:** Estimates when an error budget or SLA will be breached based on current trends and historical context.
- **Contextual Reasoning:** Explains *why* a service is at risk (e.g., "Latency is spiking similarly to Incident INC-102").

### 4. Enforcement & Remediation
Based on the high-confidence analysis, the framework can:
- **Trigger Alerts:** Notify SRE channels with a human-readable summary.
- **Block Deployments:** Enforce "Stop-Ship" signals if the error budget is exhausted.
- **Auto-Remediate:** Trigger Kubernetes drains or restarts via the integrated controller.

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
