from googleapiclient.discovery import build
from src.utils import get_key
import datetime
class PlayList:
    api_key = get_key()
    def __init__(self,id_playlist):
        self.id_playlist = id_playlist
        result = self.get_playlist().playlists().list(id=id_playlist,
                                     part='snippet,contentDetails',
                                     maxResults=50,).execute()

        self.title = result['items'][0]['snippet']['title']
        self.url = result['items'][0]['snippet']['thumbnails']['default']['url']


    @classmethod
    def get_playlist(cls):
        service = build('youtube', 'v3', developerKey=cls.api_key)
        return service

    def __str__(self):
        return f"{self.title}"

    def show_best_video(self):
        max_like = 0  # счетчик для лайков видео
        playlist_videos = self.get_playlist().playlistItems().list(playlistId=self.id_playlist,
                                               part='contentDetails',maxResults=50,).execute()
        video_ids: list[str] = [video['contentDetails']['videoId'] for video in playlist_videos['items']]
        for i in video_ids:
            video_response = self.get_playlist().videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                                               id=i).execute()
            video_like = int(video_response['items'][0]['statistics']['likeCount'])
            video_url = video_response['items'][0]['snippet']['thumbnails']['default']['url']
            if video_like > max_like:
                max_like = video_like
                best_video = video_url
        return print(f"Видео с самым большим количеством лайков {max_like} - {best_video}")

    def total_duration(self):
        count_hour = 0
        count_min = 0
        count_sec = 0
        playlist_videos = self.get_playlist().playlistItems().list(playlistId=self.id_playlist,
                                                                   part='contentDetails', maxResults=50, ).execute()
        video_ids: list[str] = [video['contentDetails']['videoId'] for video in playlist_videos['items']]
        for i in video_ids:
         video_response = self.get_playlist().videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                                           id=i).execute()
         new_v = video_response['items'][0]['contentDetails']['duration'].replace('H', ':').replace('M', ':').replace('S', '').replace('PT', '')
         if len(new_v) <= 5 and  len(new_v) >=4:
             format = '%M:%S'
             v_duration = datetime.datetime.strptime(new_v, format)
             count_min += int(v_duration.minute)
             count_sec += int(v_duration.second)
         elif len(new_v) > 5:
             format = '%H:%M:%S'
             v_duration = datetime.datetime.strptime(new_v, format)
             count_min += int(v_duration.minute)
             count_sec += int(v_duration.second)
             count_hour += int(v_duration.hour)
         elif len(new_v) <= 3:
             v = new_v.replace(":", "")
             format = '%M'
             v_duration = datetime.datetime.strptime(v, format)
             count_min += int(v_duration.minute)

         delta = datetime.timedelta(days=0,
                                   seconds=count_sec,
                                   microseconds=0,
                                   milliseconds=0,
                                   minutes=count_min,
                                   hours=count_hour,
                                   weeks=0)

        return print(f"Общая продолжительность плеейлиста составит {delta}")

























