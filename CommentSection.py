import pandas as pd

from googleapiclient.discovery import build

class CommentSection:
    def __init__(self, apiKey: str) -> None:
        self.api_key = apiKey

    def pull_comments_from_channel(self, videoId) -> object:
        """ This method will pull down the comments from a specific 
        youtube channel's video using the Youtube API """

        youtube = build('youtube','v3', developerKey=self.apiKey)

        responses = youtube.commentThreads().list(
            part = 'snippet,replies',
            videoId = videoId
        ).execute()

        return responses
