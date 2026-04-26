import requests
from backend.config import JIRA_URL, EMAIL, API_TOKEN, PROJECT_KEY


def create_jira_ticket(title, description, priority):
    url = f"{JIRA_URL}/rest/api/3/issue"

    auth = (EMAIL, API_TOKEN)

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    payload = {
        "fields": {
            "project": {
                "key": PROJECT_KEY
            },
            "summary": title,
            "description": {
                "type": "doc",
                "version": 1,
                "content": [
                    {
                        "type": "paragraph",
                        "content": [
                            {
                                "text": description,
                                "type": "text"
                            }
                        ]
                    }
                ]
            },
            "issuetype": {
                "name": "Task"
            }
        }
    }

    response = requests.post(url, json=payload, headers=headers, auth=auth)

    if response.status_code == 201:
        return response.json()["key"]
    else:
        return "Error: " + response.text