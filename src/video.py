from googleapiclient.discovery import build
from src.utils import get_key
class Video:

    api_key = get_key()
    def __init__(self, video_id: str) -> None:
        try:
            self.video_id = video_id
            result = self.get_video().videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                       id=self.video_id).execute()
            raw_data = result['items'][0]['snippet']
            self.id_video = raw_data['channelId']
            self.title = raw_data['title']
            self.url = raw_data['thumbnails']['default']['url']
            self.view_count = result['items'][0]['statistics']['viewCount']
            self.like_count = result['items'][0]['statistics']['likeCount']
        except IndexError:
            print("Неправильный id видео")
            self.video_id = video_id
            self.id_video = None
            self.title = None
            self.url = None
            self.view_count = None
            self.like_count = None





    @classmethod
    def get_video(cls):
        service = build('youtube', 'v3', developerKey=cls.api_key)
        return service

    def __str__(self):
        return f"{self.title}"

class PLVideo(Video):
    def __init__(self,video_id,id_play_list):
        super().__init__(video_id)
        self.id_play_list = id_play_list


