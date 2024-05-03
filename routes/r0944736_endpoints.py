from fastapi import APIRouter, HTTPException
from typing import List
from ..queries import r0944736_queries
from ..models import CommunityPost

router = APIRouter()

# @router.get("/")
# def root():
#     return {"message": "Hello from routes!"}

# @router.post("/submit-form")
# async def submit_form(post: CommunityPost):
#     post_id = await r0944736_queries.create_community_post(post)
#     return {"post_id": post_id, "message": "Post created successfully"}

# @router.get("/community/posts/", response_model=List[CommunityPost])
# async def get_community_posts():
#     posts = await r0944736_queries.get_community_posts()
#     if not posts:
#         raise HTTPException(status_code=404, detail="No community posts found")
#     return posts

# I'm a change hopefully