#1 import required libraries
import json
from csv import writer
from googleapiclient.discovery import build

#2 configure function parameters for required variables to pass to service
def get_comments(part='snippet', 
                 maxResults=100, 
                 textFormat='plainText',
                 order='time',
                 videoId='OQij6GB2FA8',
                 csv_filename="blackpink"):

    #3 create empty lists to store desired information
    comments, commentsId, repliesCount, likesCount, viewerRating = [], [], [], [], []
       
    # build our service from path/to/apikey
    service = build('client_secret_desktop.json')
    
    #4 make an API call using our service
    response = service.commentThreads().list(
        part=part,
        maxResults=maxResults,
        textFormat=textFormat,
        order=order,
        videoId=videoId
    ).execute()
                 

    while response: # this loop will continue to run until you max out your quota
                 
        for item in response['items']:
            #5 index item for desired data features
            comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
            comment_id = item['snippet']['topLevelComment']['id']
            reply_count = item['snippet']['totalReplyCount']
            like_count = item['snippet']['topLevelComment']['snippet']['likeCount']
            
            #6 append to lists
            comments.append(comment)
            commentsId.append(comment_id)
            repliesCount.append(reply_count)
            likesCount.append(like_count)

            #7 write line by line
            with open(f'{csv_filename}.csv', 'a+') as f:
                # https://thispointer.com/python-how-to-append-a-new-row-to-an-existing-csv-file/#:~:text=Open%20our%20csv%20file%20in,in%20the%20associated%20csv%20file
                csv_writer = writer(f)
                csv_writer.writerow([comment, comment_id, reply_count, like_count])
        
        #8 check for nextPageToken, and if it exists, set response equal to the JSON response
        if 'nextPageToken' in response:
            response = service.commentThreads().list(
                part=part,
                maxResults=maxResults,
                textFormat=textFormat,
                order=order,
                videoId=videoId,
                pageToken=response['nextPageToken']
            ).execute()
        else:
            break

    #9 return our data of interest
    return {
        'Comments': comments,
        'Comment ID': commentsId,
        'Reply Count' : repliesCount,
        'Like Count' : likesCount
    }
  