import json
from googleapiclient.discovery import build
from src.utils import  get_key



class Channel:
    """Класс для ютуб-канала"""
    api_key = get_key()

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id
        result = self.get_service().channels().list(id=self.channel_id,
                                                    part="snippet,contentDetails,statistics").execute()
        raw_data = result["items"][0]
        self.title = raw_data['snippet']['title']
        self.description = raw_data['snippet']['description']
        self.url = f"https://www.youtube.com/channel/{self.channel_id}"
        self.subscribers = int(raw_data['statistics']['subscriberCount'])
        self.video_count = int(raw_data['statistics']['videoCount'])
        self.view_count = int(raw_data['statistics']['viewCount'])

    def __str__(self):
        return f"{self.title} -  {self.url}"

    def __add__(self, other):
        """Метод сложения подписчиков"""
        if not isinstance(other, Channel):
            raise ValueError('Складывать можно только два объекта Channel.')
        return self.subscribers + other.subscribers

    def __sub__(self, other):
        """Метод вычитания подписчиков"""
        if not isinstance(other, Channel):
            raise ValueError('Вычитать можно только два объекта Channel.')
        return self.subscribers - other.subscribers

    def __eq__(self, other):
        if not isinstance(other, Channel):
            raise ValueError('Сравнивать можно только два объекта Channel.')
        return self.subscribers == other.subscribers

    def __ne__(self, other):
        if not isinstance(other, Channel):
            raise ValueError('Сравнивать можно только два объекта Channel.')
        return self.subscribers != other.subscribers

    def __lt__(self, other):
        if not isinstance(other, Channel):
            raise ValueError('Сравнивать можно только два объекта Channel.')
        return self.subscribers < other.subscribers

    def __le__(self, other):
        if not isinstance(other, Channel):
            raise ValueError('Сравнивать можно только два объекта Channel.')
        return self.subscribers <= other.subscribers

    def __gt__(self, other):
        if not isinstance(other, Channel):
            raise ValueError('Сравнивать можно только два объекта Channel.')
        return self.subscribers > other.subscribers

    def __ge__(self, other):
        if not isinstance(other, Channel):
            raise ValueError('Сравнивать можно только два объекта Channel.')
        return self.subscribers >= other.subscribers

    @classmethod
    def get_service(cls):
        service = build('youtube', 'v3', developerKey=cls.api_key)
        return service

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        print(f"Название канала: {self.title}")
        print(f"Описание канала: {self.description}")
        print(f"Ссылка на канал: {self.url}")
        print(f"Количество подписчиков: {self.subscribers}")
        print(f"Количество видео: {self.video_count}")
        print(f"Общее количество просмотров: {self.view_count}")

    def to_json(self, filename):
        """ Cохраняет в файл значения атрибутов экземпляра `Channel"""
        inform = {"Название канала": self.title,
                  "Описание канала": self.description,
                  "Ссылка на канал": self.url,
                  "Количество подписчиков": self.subscribers,
                  "Количество видео": self.video_count,
                  "Общее количество просмотров": self.view_count}

        with open(filename, "w") as file:
            json.dump(inform, file)







