import os
from googleapiclient.discovery import build


class Video:
    def __init__(self, video_id):
        self.video_id = video_id
        self.video_dict = Video.get_service().videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                                            id=video_id).execute()
        self.video_title: str = self.video_dict['items'][0]['snippet']['title']
        self.view_count: int = self.video_dict['items'][0]['statistics']['viewCount']
        self.like_count: int = self.video_dict['items'][0]['statistics']['likeCount']
        self.comment_count: int = self.video_dict['items'][0]['statistics']['commentCount']


    def __repr__(self):
        return f'{self.__class__.__name__},{self.video_id},{self.video_title},{self.like_count},{self.comment_count}'

    def __str__(self):
        return f'{self.video_title}'

    @classmethod
    def get_service(cls):
        api_key: str = os.getenv('YT_API_KEY')
        api_object = build('youtube', 'v3', developerKey=api_key)
        return api_object


class PLVideo(Video):
    def __init__(self, video_id, playlist_id):
        super().__init__(video_id)
        self.playlist_id = playlist_id

    def __repr__(self):
        return f'{self.__class__.__name__},{self.video_id},{self.video_title},{self.like_count},{self.comment_count}, {self.playlist_id}'

    def __str__(self):
        return super().__str__()
