import yaml
import time
from agents.rag_agent import RAGAgent
from agents.slo_engine import SLOEngine

def load_config(path="config/slos.yaml"):
    with open(path, 'r') as f:
        return list(yaml.safe_load_all(f))

def main():
    # 1. Initialize RAG and SLO Engines
    rag = RAGAgent()
    engine = SLOEngine(model="gpt-4", rag_agent=rag)

    # Pre-populate RAG Knowledge Base (Context)
    rag.add_knowledge(
        documents=["SLA for payment-api requires 99.9% uptime for enterprise customers.", 
                   "Historical incident INC-2024-001 showed peak-hour latency spikes on Fridays."],
        metadatas=[{"type": "SLA"}, {"type": "Incident"}],
        ids=["doc1", "doc2"]
    )

    # 2. Load SLO/SLA Definitions (OpenSLO-inspired)
    configs = load_config()
    print(f"Loaded {len(configs)} SLO/SLA configurations.")

    # 3. Simulate continuous monitoring loop
    while True:
        # Mocking SLI Data from OpenTelemetry
        mock_slis = {
            "http_requests_total": 10000,
            "http_requests_success": 9985, # 99.85% (at risk of 99.9% SLO)
            "latency_p99_ms": 150
        }

        print("\n--- Calculating Internal SLO/SLA Health ---")
        for config in configs:
            if config.get('kind') == 'SLO':
                health = engine.calculate_health(mock_slis, config)
                print(f"Service: {config['metadata']['service']}")
                print(f"Status: {health['status']}")
                print(f"Analysis: {health['raw_analysis']}")

        time.sleep(60) # Poll every minute

if __name__ == "__main__":
    main()
