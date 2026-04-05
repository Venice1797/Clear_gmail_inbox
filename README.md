# Clear_gmail_inbox

What it says! 

Odd that FAGoogle doesn't have it built in, one wonders why...

# Build & Run steps:

This is very rough, not for general audiance, it did work for me.

## install python modules from FAGoogle
pip install google-api-python-client google-auth-httplib2 google-auth-oauthlib

## Get OAuth creds
One-time OAuth setup:
Step 1: Get a credentials.json from Google

Go to console.cloud.google.com, you will have to enable 2FA, FAGoogle!

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

## Run the python scritp, 
FAGoogle will complain alot, warn alot, ignore it, you are running your own app to cleanup inbox, a critically missing feature from FAGoogle, that I speculate (pretty sure) it is intentionally missing.
