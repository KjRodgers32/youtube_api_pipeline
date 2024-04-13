import pandas as pd

class CommentRepliesMap:
    def __init__(self):
        self.comments = []
        self.commentReplyMap = {}
    
    def append(self, comment: str, replies: list) -> None:
        arr_index = len(self.comments)
        self.commentReplyMap[arr_index] = replies
        self.comments.append(comment)

    def printMap(self) -> None:
        for i in range(len(self.comments)):
            print(f"{self.comments[i]}: {self.commentReplyMap[i]}")

    def printMapByIndex(self, index: int) -> None:
        if index < 0 or index >= len(self.comments):
            raise IndexError("Index out of range")
        print(f"{self.comments[index]}: {self.commentReplyMap[index]}")