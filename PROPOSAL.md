# Kube-SRE-Vantage: AI-Powered Infrastructure Reliability Framework

## Overview
**Kube-SRE-Vantage** is a Python-based framework designed to automate the lifecycle of Production Engineering. It integrates **OpenTelemetry (OTel)** for vendor-neutral observability and **Generative AI (LLMs/SLMs)** to manage SRE KPIs across cloud-managed Kubernetes environments (AKS, EKS, GKE).

## Core SRE KPIs Addressed
1.  **SLO Attainment (Availability & Latency):** Real-time tracking of user-facing performance.
2.  **MTTR (Mean Time To Repair):** Reduced via AI-driven Root Cause Analysis (RCA).
3.  **Error Budget Consumption:** Automated "Stop-Ship" signals based on remaining budget.
4.  **Infrastructure Efficiency:** OTel-driven rightsizing and thermal-aware scheduling.

## Technical Architecture (Python + Kubernetes)

### 1. The OTel Collector & Processor (Python SDK)
- Uses the `opentelemetry-sdk` to ingest metrics and traces from the cluster.
- **Feature:** Standardizes data from Cloud-managed hardware (e.g., AWS Nitro, Azure Boost) into a unified format.

### 2. The "Vantage" Engine (GenAI Layer)
- **RCA Agent:** Uses an LLM (Llama 3, GPT-4, or Claude) to analyze "Trace Deltas." When an SLO is breached, the agent compares current traces against "Golden Traces" and generates a human-readable diagnosis.
- **SLM Log Analyzer:** A Small Language Model (SLM) runs as a sidecar to analyze high-volume K8s events and node-level logs for pre-failure hardware signatures.

### 3. Kubernetes Controller (Remediation)
- Built with `kopf` (Kubernetes Operator Framework) or `kubernetes-python`.
- **Feature:** Automatically executes "Drains" or "Restarts" only when the Vantage Engine confirms a high-confidence diagnosis.

## Project Structure (Python)
```text
kube-sre-vantage/
├── agents/
│   ├── rca_agent.py          # LLM Logic for Root Cause Analysis
│   └── health_monitor.py     # OTel Metric & Trace processor
├── controllers/
│   ├── slo_controller.py     # K8s Operator for SLO enforcement
│   └── remediation_ops.py    # Automated actions (drain, scale, restart)
├── api/
│   └── v1/                   # REST API for SRE Dashboard
├── config/
│   ├── slos.yaml             # Define your Availability/Latency targets
│   └── otel_config.yaml      # OpenTelemetry Collector settings
└── main.py                   # Framework entry point
```

## Cloud Agnostic Features
- **EKS (AWS):** Integrates with AWS Distro for OpenTelemetry (ADOT).
- **AKS (Azure):** Connects to Azure Monitor and Managed Grafana via OTel.
- **GKE (GCP):** Leverages Google Cloud Trace and Operations Suite.

## Production Engineering Focus
This framework moves beyond "Alerting" to "Understanding." By using LLMs to parse the complex relationship between infrastructure logs and application traces, it reduces the cognitive load on SREs during "on-call" shifts.
