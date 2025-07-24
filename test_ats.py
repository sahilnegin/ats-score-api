from ats_score import calculate_ats_score

def test_ats_score_basic():
    resume = "Experienced with React, FastAPI, AWS"
    jd = "Looking for a developer skilled in React and FastAPI"
    result = calculate_ats_score(resume, jd)
    assert "ats_score" in result
    assert result["ats_score"] > 0
