from googleapiclient.discovery import build
from src.utils import get_key
class PlayList:
    api_key = get_key()
    def __init__(self,id_playlist):
        self.id_playlist = id_playlist
        result = self.get_playlist().playlists().list(channelId=id_playlist,
                                     part='contentDetails,snippet',
                                     maxResults=50,
                                     ).execute()
        print(result)


    @classmethod
    def get_playlist(cls):
        service = build('youtube', 'v3', developerKey=cls.api_key)
        return service

    def __str__(self):
        return f"{self.title}"


pl = PlayList('PLv_zOGKKxVpj-n2qLkEM2Hj96LO6uqgQw')