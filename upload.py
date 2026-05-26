import os
import pickle

from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.auth.transport.requests import Request

SCOPES = [
    "https://www.googleapis.com/auth/youtube.upload"
]

CLIENT_SECRET_FILE = "client_secret.json"

VIDEO_FILE = "final.mp4"

TITLE = "Jesus Walked On Water 😱 #shorts"

DESCRIPTION = """
Amazing Bible Story Shorts

#Jesus
#Bible
#Christian
#Shorts
"""

def authenticate():

    creds = None

    if os.path.exists("token.pickle"):

        with open("token.pickle", "rb") as token:
            creds = pickle.load(token)

    if not creds or not creds.valid:

        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())

        else:

            flow = InstalledAppFlow.from_client_secrets_file(
                CLIENT_SECRET_FILE,
                SCOPES
            )

            creds = flow.run_console()

        with open("token.pickle", "wb") as token:
            pickle.dump(creds, token)

    return creds

def upload_video():

    creds = authenticate()

    youtube = build(
        "youtube",
        "v3",
        credentials=creds
    )

    request = youtube.videos().insert(
        part="snippet,status",

        body={

            "snippet": {
                "title": TITLE,
                "description": DESCRIPTION,
                "tags": [
                    "Jesus",
                    "Bible",
                    "Christian",
                    "Shorts"
                ],
                "categoryId": "22"
            },

            "status": {
                "privacyStatus": "public",
                "selfDeclaredMadeForKids": False
            }
        },

        media_body=MediaFileUpload(
            VIDEO_FILE,
            resumable=True
        )
    )

    response = request.execute()

    print("UPLOAD SUCCESS")
    print(response)

upload_video()