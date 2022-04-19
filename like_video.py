import argparse
import os
import re
import json

import google.oauth2.credentials
import google_auth_oauthlib.flow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google_auth_oauthlib.flow import InstalledAppFlow

CLIENT_SECRETS_FILE = 'client_secret_desktop.json'

SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']
API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3'

RATINGS = ('like', 'dislike', 'none')

def get_authenticated_service():
  flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
  print(flow)
  try: 
    credentials = flow.run_console()
  except:
    print("error")
    # print ('An HTTP error %d occurred:\n%s' % (e.resp.status, e.content))

  print(credentials.client_id)
  print(credentials.client_secret)
  print(credentials.expiry)
  print(credentials.refresh_token)
  print(credentials.token)

  return build(API_SERVICE_NAME, API_VERSION, credentials = credentials)


def like_video(youtube, args):
  for arg in args:
    youtube.videos().rate(
      id=arg.videoId,
      rating=arg.rating
    ).execute()


if __name__ == '__main__':
  args = []
  parser = argparse.ArgumentParser()
  parser.add_argument('--videoId', default='OQij6GB2FA8',
    help='ID of video to like.')
  parser.add_argument('--rating', default='like',
    choices=RATINGS,
    help='Indicates whether the rating is "like", "dislike", or "none".')

  args.append(parser.parse_args())

  parser = argparse.ArgumentParser()
  parser.add_argument('--videoId', default='uQchPj8T5M8',
    help='ID of video to like.')
  parser.add_argument('--rating', default='like',
    choices=RATINGS,
    help='Indicates whether the rating is "like", "dislike", or "none".')

  args.append(parser.parse_args())

  # print(args)

  youtube = get_authenticated_service()
  try:
    like_video(youtube, args)
  except HttpError as e:
    print ('An HTTP error %d occurred:\n%s' % (e.resp.status, e.content))
  else:
    for arg in args:
      print ('The %s rating has been added for video ID %s.' %
           (arg.rating, arg.videoId))