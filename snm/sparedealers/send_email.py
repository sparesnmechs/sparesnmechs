import requests
from django.conf import settings


def send_simple_message(message, email):
    """Send a request to the admin."""
    domain = settings.MG_DOMAIN
    return requests.post(
        settings.MG_URL,
        auth=("api", settings.MG_API),
        data={
            "from": f"{email} <{domain}>",
            "to": [settings.MG_DEFAULT_EMAIL],
            "subject": "Request For a Part",
            "text": message,
        },
    )
