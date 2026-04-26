from backend.jira_service import create_jira_ticket


def extract_details(user_input):
    text = user_input.strip()

    # Remove common prefix words
    cleaned = text.lower()
    cleaned = cleaned.replace("create jira ticket for", "")
    cleaned = cleaned.replace("create ticket for", "")
    cleaned = cleaned.replace("jira ticket for", "")

    cleaned = cleaned.strip().capitalize()

    # Title = first 6 words (clean & short)
    words = cleaned.split()
    title = " ".join(words[:6])

    # Priority detection
    priority = "Medium"
    if "fail" in text.lower() or "error" in text.lower():
        priority = "High"

    return title, user_input, priority

def run_agent(user_input):
    title, description, priority = extract_details(user_input)

    issue_key = create_jira_ticket(title, description, priority)

    return issue_key