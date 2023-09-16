from googleapiclient.discovery import build
from pprint import PrettyPrinter


def get_video_links_by_keyword(keyword, config):
    youtube = build('youtube','v3',developerKey = config['youtube_api_key'])
    # print(type(youtube))
    request = youtube.search().list(q=keyword, part='id',type='video', maxResults=1)
    res = request.execute()
    videoId = res['items'][0]['id']['videoId']
    link = f'https://www.youtube.com/watch?v={videoId}'
    return link