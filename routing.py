TEAM_MAP = {
    "Billing": "Finance Team",
    "Technical": "Engineering Team",
    "Account": "Customer Support",
    "Security": "Security Team"
}


def assign_team(category):
    return TEAM_MAP.get(category, "Customer Support")