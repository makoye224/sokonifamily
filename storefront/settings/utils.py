import google.auth
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials


def get_oauth2_access_token():
    # Replace the client credentials with the new values
    client_credentials = {
        "client_id": "932427785269-qs9gs5k4s4j8ans38enghgrjo9hfnlnb.apps.googleusercontent.com",
        "client_secret": "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",
        "scopes": ["https://mail.google.com/"],
    }

    # Load the OAuth client credentials
    creds, project = google.auth.default()

    # Check if the credentials need a refresh
    if creds.expired and creds.refresh_token:
        creds.refresh(Request())

    # Return the access token
    return creds.token
