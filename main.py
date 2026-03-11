import yaml
import time
from agents.rag_agent import RAGAgent
from agents.slo_engine import SLOEngine
from agents.security_agent import SecurityVantageAgent

def load_config(path="config/slos.yaml"):
    with open(path, 'r') as f:
        return list(yaml.safe_load_all(f))

def main():
    # 1. Initialize RAG, SLO, and Security Engines
    rag = RAGAgent()
    engine = SLOEngine(model="gpt-4", rag_agent=rag)
    security = SecurityVantageAgent(model="gpt-4")

    # Pre-populate Knowledge (SLA + Security Baselines)
    rag.add_knowledge(
        documents=[
            "SLA for payment-api: 99.9% uptime for enterprise customers.", 
            "Zero-Trust Baseline: All admin actions must use JIT tokens with 1-hour TTL.",
            "Threat Model T-102: Data Exfiltration via over-privileged AI agents."
        ],
        metadatas=[{"type": "SLA"}, {"type": "Security"}, {"type": "ThreatModel"}],
        ids=["doc1", "doc2", "doc3"]
    )

    configs = load_config()
    print(f"Loaded {len(configs)} SLO/SLA configurations.")

    while True:
        # Mocking Telemetry Data (OTel + IAM Logs)
        mock_data = {
            "slis": {
                "http_requests_total": 10000,
                "http_requests_success": 9985,
                "latency_p99_ms": 150
            },
            "security_logs": [
                {"user": "ai-agent-7", "action": "read-db", "access_type": "persistent", "time": "10:05"},
                {"user": "sre-admin-1", "action": "scale-cluster", "access_type": "jit", "time": "10:10"}
            ]
        }

        print("\n--- [ Kube-SRE-Vantage Health Check ] ---")
        
        # 1. Performance SLO Check
        for config in configs:
            if config.get('kind') == 'SLO':
                health = engine.calculate_health(mock_data['slis'], config)
                print(f"Service: {config['metadata']['service']} | Status: {health['status']}")
                print(f"AI RCA: {health['raw_analysis'][:150]}...")

        # 2. Security & Compliance Check (Google Staff Security Requirements)
        print("\n--- [ Security & Zero-Trust Check ] ---")
        sec_health = security.evaluate_zero_trust_health(mock_data['security_logs'])
        print(f"Zero-Trust Analysis: {sec_health['analysis'][:200]}...")

        time.sleep(60)

if __name__ == "__main__":
    main()
