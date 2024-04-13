import pandas as pd

class CommentSection:
    def __init__(self, video_url: str, api_key: str) -> None:
        self.page = video_url
        self.api_key = api_key
        self.comments = []
        self.replies = []

    def pull_comments_from_channel(self) -> pd.Dataframe:
        """ This method will pull down the comments from a specific 
        youtube channel's video using the Youtube API """
