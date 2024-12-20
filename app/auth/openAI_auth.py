import time
import httpx
import os

def generate_openai_token():
    auth  = os.getenv("OPENAI_AUTH_URL")
    client_id = os.getenv("OPENAI_CLIENT_ID")
    client_secret = os.getenv("OPENAI_CLIENT_SECRET")
    scope = os.getenv("OPENAI_SCOPE")
    grant_type  = "client_credentials"
    issue_time = int(time.time())

    with httpx.Client() as client:
        body = {
            "grant_type": grant_type,
            "scope": scope,
            "client_id": client_id,
            "client_secret": client_secret,
        }
        resp = client.post(auth, data=body, timeout=45)
    token = resp.json()["access_token"]
    os.environ["OPENAI_TOKEN"] = token
    os.environ["OPENAI_TOKEN_ISSUE_TIME"] = str(issue_time)
    return token


