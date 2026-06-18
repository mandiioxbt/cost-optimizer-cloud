class CostAnalyzer:
    def __init__(self, provider="aws"): self.provider = provider
    def rightsizing(self, instances):
        return [{"id": i["id"], "suggested": "t3.medium", "savings": 150}
                for i in instances if i.get("avg_cpu", 0) < 20]
    def find_idle(self, resources): return [r for r in resources if r.get("cpu", 0) < 5]
    def reserved_analysis(self, instances):
        return [{"id": i["id"], "recommendation": "1yr reserved", "savings_pct": 40}
                for i in instances if i.get("utilization", 0) > 60]
