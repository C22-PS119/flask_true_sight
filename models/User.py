from __future__ import annotations
from datetime import datetime
from database import Model


class User(Model):
    def __init__(self) -> None:
        self.set(None, '', '', '', '', datetime.now().timestamp())
        super().__init__()

    def set(self, id, username: str, full_name: str, email: str, password: str, date_created: int, verified: bool = False, apioauth: str = None, votes: str = None, bookmarks: str = None) -> User:
        self.id = id
        self.username = username
        self.full_name = full_name
        self.email = email
        self.password = password
        self.date_created = date_created
        self.apioauth = apioauth
        self.verified = verified
        self.votes = votes
        self.bookmarks = bookmarks
        return self

    def parse(data) -> User:
        # 0 -> id
        # 1 -> username
        # 2 -> full_name
        # 3 -> email
        # 4 -> apioauth
        # 5 -> password
        # 6 -> date_created
        # 7 -> verified
        # 8 -> votes
        # 9 -> bookmarks
        user = User().set(data[0], data[1], data[2], data[3], data[5], data[6], int(
            data[7]) == 1, data[4], data[8], data[9])
        return user

    def get(self):
        data = self.__dict__
        data['verified'] = 1 if data['verified'] else 0
        return data

    def fromDict(data: dict) -> User:
        user = User()
        user.__dict__ = data
        return user
