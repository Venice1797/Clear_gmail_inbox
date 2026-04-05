import os

from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials

from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

SCOPES = ['https://mail.google.com/']  # Full access needed for deletion

def get_creds():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as f:
            f.write(creds.to_json())
    return creds

creds = get_creds()

# Authenticate, then:
service = build('gmail', 'v1', credentials=creds)

while True:
    results = service.users().messages().list(userId='me', maxResults=500).execute()
    messages = results.get('messages', [])
    if not messages:
        break
    ids = [m['id'] for m in messages]
    service.users().messages().batchDelete(userId='me', body={'ids': ids}).execute()
    print(f"Deleted {len(ids)} messages")
