import json

class InspectionAgentOrchestrator:
    def __init__(self):
        self.trace_log = []

    def evaluate_and_act(self, initial_metrics: dict, image_bytes: bytes) -> dict:
        """
        Executes the Agentic Vision decision loop.
        If OpenCV returns UNCERTAIN, the agent decides to trigger a secondary tool call
        (e.g., exposure adjustment & re-scan) to change the outcome.
        """
        self.trace_log.append({
            "step": "perception",
            "input_metrics": initial_metrics
        })

        if initial_metrics["ambiguous"]:
            # Agent Decision: Adjust exposure and re-inspect
            self.trace_log.append({
                "step": "decision",
                "action": "TRIGGER_SECONDARY_ZOOM_AND_EXPOSURE_BOOST",
                "reason": "Defect score falls in ambiguous threshold; high-risk shadow suspected."
            })
            
            # Simulated tool execution outcome
            resolved_status = "CLEAR_AFTER_REINSPECTION" if initial_metrics["defect_score"] < 200 else "CONFIRMED_DEFECT"
            
            self.trace_log.append({
                "step": "action_result",
                "final_status": resolved_status
            })
            
            return {
                "decision_made": True,
                "action_taken": "Adjusted exposure & re-evaluated via OpenCV 5",
                "status": resolved_status,
                "trace": self.trace_log
            }
        
        return {
            "decision_made": False,
            "action_taken": "None (Clear/Defect confidence high)",
            "status": initial_metrics["status"],
            "trace": self.trace_log
        }
