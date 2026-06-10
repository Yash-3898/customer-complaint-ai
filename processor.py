import pandas as pd

from classifier import classify_complaint
from routing import assign_team


def process_complaint(complaint):
    result = classify_complaint(complaint)

    team = assign_team(result["category"])

    return {
        "complaint": complaint,
        "category": result["category"],
        "priority": result["priority"],
        "team": team
    }


def process_complaints(complaints):
    results = []

    for complaint in complaints:
        results.append(process_complaint(complaint))

    return pd.DataFrame(results)