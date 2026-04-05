# Clear_gmail_inbox

What it says! 

Odd that FAGoogle doesn't have it built in, one wonders why...

# Build & Run steps:

This is very rough, not for general audiance, it did work for me.

pip install google-api-python-client google-auth-httplib2 google-auth-oauthlib

One-time OAuth setup:
Step 1: Get a credentials.json from Google

Go to console.cloud.google.com
Create a project → Enable Gmail API
Go to APIs & Services → Credentials → Create Credentials → OAuth 2.0 Client ID
Application type: Desktop app
Download the JSON → save as credentials.json in your script folder

OAuth consent screen — just fill in:

App name: anything!
User support email: your email
Developer contact email: your email
Everything else: skip/leave blank

Audience — set to External 
