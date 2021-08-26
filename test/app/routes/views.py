from __future__ import annotations

from app.models.Post import Post

from fastapi import APIRouter

from app.apis.write_post.mainmod import write_post
from app.apis.get_post.mainmod import list_posts
from app.apis.get_post.mainmod import get_post

router = APIRouter()

@router.get("/", tags=["list_posts"])
async def get_home() -> bool:
    return list_posts()

@router.post("/write_post", tags=["write_posts"])
async def get_home(post: Post) -> bool:
    return write_post(post)

@router.get("/{id}", tags=["get_post"])
async def get_post(id: int) -> bool:
    return get_post(id)
