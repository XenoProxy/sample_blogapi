# uvicorn main:app --reload
import fastapi
from typing import List

from db.validation import Post, PostIn
from db.models import posts
from db.connection import database

app = fastapi.FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.get('/posts/', response_model=List[Post])
async def read_posts():
    query = posts.select()
    return await database.fetch_all(query)


@app.post('/posts', response_model=Post)
async def create_post(post: PostIn):
    query = posts.insert().values(
        title=post.title,
        text=post.text,
        is_published=post.is_published,
    )
    last_record_id = await database.execute(query)
    return {**post.dict(), "id": last_record_id}


@app.delete('/post/{post_id}')
async def delete_post(post_id: int):
    query = posts.delete().where(id == post_id)
    await database.execute(query)
    return {"detail": "Post deleted", "status_code": 204}

