import json
import os

import googleapiclient.discovery
# необходимо установить через: pip install google-api-python-client
from googleapiclient.discovery import build

import isodate

api_key: str = os.getenv('YT_API_KEY')
youtube = build('youtube', 'v3', developerKey=api_key)



class Channel:
    """Класс для ютуб-канала"""
    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id
        self.channel_dict = youtube.channels().list(id=self.__channel_id, part='snippet,statistics').execute()
        self.title = self.channel_dict['items'][0]['snippet']['title']
        self.video_count = self.channel_dict['items'][0]['statistics']['videoCount']
        self.url = f"https://www.youtube.com/channel/{self.channel_dict['items'][0]['id']}"
        self.subsribers_count = self.channel_dict['items'][0]['statistics']['subscriberCount']
        self.views_count = self.channel_dict['items'][0]['statistics']['viewCount']
        self.description = self.channel_dict['items'][0]['snippet']['description']

    @classmethod
    def get_service(cls):
        return googleapiclient.discovery.Resource

    def to_json(self, json_file):
        channel_data = [self.__channel_id, self.title, self.description, self.url, self.subsribers_count, self.video_count, self.views_count]
        with open(json_file, 'w', encoding='utf-8') as file:
            json.dump(channel_data, file, ensure_ascii=False)


    #self.channel_dict = youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        #channel_dict = youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        print(json.dumps(self.channel_dict, indent=2, ensure_ascii=False))
