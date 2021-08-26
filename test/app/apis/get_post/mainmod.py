from __future__ import annotations
from app.models.Post import Post
from typing import List
from app.models.mongo_client import posts

def list_posts() -> List:
    result = posts.find()
    return result

def get_post(id: int) -> Post:
    post = posts.find_one({"id": id})
    return post
