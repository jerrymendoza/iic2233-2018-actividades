import httplib2
import os

from apiclient import discovery, errors
import oauth2client
from oauth2client import client
from oauth2client import tools

import base64
from email.mime.text import MIMEText

mailto = "jmendoza.jerry@gmailcom"


SCOPES = 'https://www.googleapis.com/auth/gmail.compose'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Gmail API Python Test'

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

def SendMessage(service, user_id, message):
    try:
      message = (service.users().messages().send(userId=user_id, body=message)
               .execute())
      print ('Message Id: %s' % message['id'])
      return message
    except errors.HttpError as error:
      print ('An error occurred: %s' % error)

def get_credentials(): 
    credential_dir = '/home/username/gmailApp'
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'gmail-python-test.json')

    store = oauth2client.file.Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: 
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials

def create_message(sender, to, subject, message_text):
    message = MIMEText(message_text)
    message['to'] = to
    message['from'] = sender
    message['subject'] = subject
    raw = base64.urlsafe_b64encode(bytes(str(message), "utf-8"))
    return {'raw': raw.decode()}

def main( sender, recepient, subject, text_body ):
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('gmail', 'v1', http=http)
    testMessage = create_message( sender, recepient, subject, text_body )
    SendMessage( service, sender, testMessage )

if __name__ == '__main__':
    main( 'me', mailto, 'Test mail subject', 'Test mail body' )