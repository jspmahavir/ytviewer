from youtube_transcript_api import YouTubeTranscriptApi
scriptRes = ''
video_id = 'uQchPj8T5M8'
try:
    res = ''
    responses = YouTubeTranscriptApi.get_transcript(video_id)
    print('\n'+"Video: "+"https://www.youtube.com/watch?v="+str(video_id)+'\n'+'\n'+"Captions:")
    for response in responses:
        text = response['text']
        res += " "+ text
        # print(text)
    transcript = res.replace("[Music]", " ")
    scriptRes = transcript.replace("   ", " ")
except Exception as e:
    print(e)

print(scriptRes)