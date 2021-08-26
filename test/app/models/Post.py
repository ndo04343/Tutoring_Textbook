from pydantic import BaseModel

class Post(BaseModel):
    writer: str
    title: str
    body: str
    like: int
    datetime: str