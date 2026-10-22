import pytest
from agent.mcp_tools import AgenticVisionOrchestrator

def test_agent_ambiguous_loop():
    orchestrator = AgenticVisionOrchestrator()
    ambiguous_metrics = {
        "status": "REVIEW_REQUIRED",
        "defect_area_px": 250.0,
        "contour_count": 2,
        "ambiguous_flag": True,
        "engine": "COOL-OpenCV5-Arm64"
    }
    res = orchestrator.run_perception_loop(ambiguous_metrics)
    assert res["autonomous_action_taken"] == True
    assert len(res["trace"]) >= 3
