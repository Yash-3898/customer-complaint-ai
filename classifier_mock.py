def classify_complaint(complaint: str):
    """
    Mock AI classifier using keyword matching.
    Returns category and priority.
    """

    text = complaint.lower()

    # Determine Category
    if any(word in text for word in [
        "payment",
        "refund",
        "charged",
        "billing",
        "invoice",
        "deducted",
        "transaction"
    ]):
        category = "Billing"

    elif any(word in text for word in [
        "bug",
        "error",
        "crash",
        "technical",
        "loading",
        "failed"
    ]):
        category = "Technical"

    elif any(word in text for word in [
        "hack",
        "hacked",
        "unauthorized",
        "password",
        "breach",
        "security",
        "suspicious"
    ]):
        category = "Security"

    else:
        category = "Account"

    # Determine Priority
    if any(word in text for word in [
        "urgent",
        "immediately",
        "critical",
        "hack",
        "hacked",
        "breach",
        "unauthorized"
    ]):
        priority = "Critical"

    elif any(word in text for word in [
        "refund",
        "deducted",
        "charged",
        "cannot",
        "can't",
        "unable"
    ]):
        priority = "High"

    elif any(word in text for word in [
        "issue",
        "problem",
        "delay",
        "crash",
        "error",
        "failed"
    ]):
        priority = "Medium"

    else:
        priority = "Low"

    return {
        "category": category,
        "priority": priority
    }