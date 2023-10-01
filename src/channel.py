import json
import os
from googleapiclient.discovery import build

api_key = "AIzaSyAWvYvv5cT7KYlK-WtJSVA0CEfw_D02ZkE"
class Channel:
    """Класс для ютуб-канала"""


    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id
        result = self.get_service().channels().list(id=self.channel_id, part="snippet,contentDetails,statistics").execute()
        raw_data = result["items"][0]
        self.title = raw_data['snippet']['title']
        self.description = raw_data['snippet']['description']
        self.url = f"https://www.youtube.com/channel/{self.channel_id}"
        self.subscribers = int(raw_data['statistics']['subscriberCount'])
        self.video_count = int(raw_data['statistics']['videoCount'])
        self.view_count = int(raw_data['statistics']['viewCount'])

    def get_service(self):
        service = build('youtube', 'v3', developerKey=api_key)
        return service



    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        print(f"Название канала: {self.title}")
        print(f"Описание канала: {self.description}")
        print(f"Ссылка на канал: {self.url}")
        print(f"Количество подписчиков: {self.subscribers}")
        print(f"Количество видео: {self.video_count}")
        print(f"Общее количество просмотров: {self.view_count}")




