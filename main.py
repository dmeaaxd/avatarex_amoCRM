import requests

base_url = "https://api.avatarex.com"


def signup(email, account_id):
    endpoint = "/signup"
    url = f"{base_url}{endpoint}"
    data = {"email": email, "account_id": account_id}
    response = requests.post(url, json=data)
    return response.json()


def signin(email, password, account_id):
    endpoint = "/signin"
    url = f"{base_url}{endpoint}"
    data = {"email": email, "password": password, "account_id": account_id}
    response = requests.post(url, json=data)
    return response.json()


def get_profile(account_id):
    endpoint = "/profile"
    url = f"{base_url}{endpoint}"
    data = {"account_id": account_id}
    response = requests.post(url, json=data)
    return response.json()


def signout(account_id):
    endpoint = "/signout"
    url = f"{base_url}{endpoint}"
    data = {"account_id": account_id}
    response = requests.post(url, json=data)
    return response.json()


def send_form(account_id, form, email, phone, text):
    endpoint = "/form"
    url = f"{base_url}{endpoint}"
    data = {
        "account_id": account_id,
        "form": form,
        "email": email,
        "phone": phone,
        "text": text
    }
    response = requests.post(url, json=data)
    return response.json()


def activate_webhook(account_id, phone, name, email, domain, user_count):
    endpoint = "/webhooks/activate"
    url = f"{base_url}{endpoint}"
    data = {
        "account_id": account_id,
        "phone": phone,
        "name": name,
        "email": email,
        "domain": domain,
        "user_count": user_count
    }
    response = requests.post(url, json=data)
    return response.json()


def deactivate_webhook(account_id):
    endpoint = "/webhooks/deactivate"
    url = f"{base_url}{endpoint}"
    data = {"account_id": account_id}
    response = requests.post(url, json=data)
    return response.json()


def event_webhook(account_id, channel_uuid, message_type, meta_text, meta_content_url, lead_data):
    endpoint = "/webhooks/event"
    url = f"{base_url}{endpoint}"
    data = {
        "event": {
            "account_id": account_id,
            "chat": {
                "channel_uuid": channel_uuid
            },
            "message": {
                "type": message_type,
                "meta": {
                    "text": meta_text,
                    "content_url": meta_content_url
                }
            },
            "lead": lead_data
        }
    }
    response = requests.post(url, json=data)
    return response.json()


def token_webhook(account_id):
    endpoint = "/token"
    url = f"{base_url}{endpoint}"
    data = {"account_id": account_id}
    response = requests.post(url, json=data)
    return response.json()
