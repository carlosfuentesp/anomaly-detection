import pickle
import os.path
import io
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.http import MediaIoBaseDownload

SCOPES = ['https://www.googleapis.com/auth/drive']


def get_file():
    credentials = get_credentials()
    filename = "log_154_2020-6-23-08-34-52.px4log.csv"

    service = build('drive', 'v3', credentials=credentials)
    file_id = search(service, filename)

    if not file_id:
        download(file_id, service)


def download(file_id, service):
    request = service.files().get_media(fileId=file_id)
    # fh = io.BytesIO() # in memory
    fh = io.FileIO('data/output/output.csv', 'wb')
    downloader = MediaIoBaseDownload(fh, request)
    done = False
    while done is False:
        status, done = downloader.next_chunk()
        print("Download %d%%." % int(status.progress() * 100))


def search(service, filename):
    while True:
        response = service.files().list(q=("name='%s'" % filename), fields='nextPageToken, files(id, name)', ).execute()
        files = response.get('files', [])
        if not files:
            return ""
        return files[0].get('id')


def get_credentials():
    credentials = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            credentials = pickle.load(token)
    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('source/ingestion/credentials.json', SCOPES)
            credentials = flow.run_local_server(port=0)
        with open('token.pickle', 'wb') as token:
            pickle.dump(credentials, token)
    return credentials
