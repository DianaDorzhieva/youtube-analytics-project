from googleapiclient.discovery import build
from src.utils import get_key
import datetime
import isodate


class PlayList:
    api_key = get_key()

    def __init__(self, id_playlist):
        self.id_playlist = id_playlist
        result = self.get_playlist().playlists().list(id=id_playlist,
                                                      part='snippet',
                                                      maxResults=50, ).execute()

        self.title = result['items'][0]['snippet']['title']
        self.url = f'https://www.youtube.com/playlist?list={self.id_playlist}'

    @classmethod
    def get_playlist(cls):
        service = build('youtube', 'v3', developerKey=cls.api_key)
        return service

    def __str__(self):
        return f"{self.title}"

    def show_best_video(self):
        max_like = 0  # счетчик для лайков видео
        playlist_videos = self.get_playlist().playlistItems().list(playlistId=self.id_playlist,
                                                                   part='contentDetails', maxResults=50, ).execute()
        video_ids: list[str] = [video['contentDetails']['videoId'] for video in playlist_videos['items']]
        for i in video_ids:
            video_response = self.get_playlist().videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                                               id=i).execute()
            video_like = int(video_response['items'][0]['statistics']['likeCount'])
            if video_like > max_like:
                max_like = video_like
                best_video = i
        return f'https://youtu.be/{best_video}'

    @property
    def total_duration(self):
        playlist_videos = self.get_playlist().playlistItems().list(playlistId=self.id_playlist,
                                                                   part='contentDetails',
                                                                   maxResults=50,
                                                                   ).execute()
        video_ids: list[str] = [video['contentDetails']['videoId'] for video in playlist_videos['items']]
        video_response = self.get_playlist().videos().list(part='contentDetails,statistics',
                                                           id=','.join(video_ids)
                                                           ).execute()
        duration = datetime.timedelta()
        for video in video_response['items']:
            iso_8601_duration = video['contentDetails']['duration']
            duration += isodate.parse_duration(iso_8601_duration)
        return duration


pl = PlayList('PLv_zOGKKxVpj-n2qLkEM2Hj96LO6uqgQw')
pl.total_duration
