from core.decision_engine import DecisionEngine

engine = DecisionEngine()

test_cases = [
    {"last_score": 0.3, "engagement": "high"},
    {"last_score": 0.6, "engagement": "high"},
    {"last_score": 0.9, "engagement": "high"},
    {"last_score": 0.8, "engagement": "low"},
]

for case in test_cases:
    print(case, "→", engine.decide_next_step(case))
