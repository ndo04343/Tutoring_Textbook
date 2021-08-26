from __future__ import annotations
from app.models.Post import Post
from app.models.mongo_client import posts

def write_post(post: Post) -> bool:
    if post:
        posts.insert_one(
            post
        )
        return True
    return False
