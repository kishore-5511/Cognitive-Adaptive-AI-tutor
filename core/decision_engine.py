class DecisionEngine:
    def decide_next_step(self, student_state: dict) -> str:
        """
        Decide which agent should handle the next step.
        """

        score = student_state.get("last_score", 0)
        engagement = student_state.get("engagement", "medium")

        # Rule 1: Low engagement
        if engagement == "low":
            return "tutor_agent"

        # Rule 2: Low score
        if score < 0.5:
            return "tutor_agent"

        # Rule 3: Medium score
        if 0.5 <= score <= 0.75:
            return "practical_agent"

        # Rule 4: High score
        if score > 0.75:
            return "monitor_agent"

        return "tutor_agent"
