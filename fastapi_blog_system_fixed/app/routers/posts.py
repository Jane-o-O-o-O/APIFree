```python
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from .. import schemas, crud, models
from ..database import get_db

router = APIRouter()

@router.get("/", response_model=List[schemas.Post], status_code=status.HTTP_200_OK)
def get_posts(db: Session = Depends(get_db)):
    """
    Retrieve all posts.
    """
    return crud.get_posts(db)

@router.post("/", response_model=schemas.Post, status_code=status.HTTP_201_CREATED)
def create_post(post: schemas.PostCreate, db: Session = Depends(get_db)):
    """
    Create a new post.
    """
    return crud.create_post(db=db, post=post)

@router.get("/{post_id}", response_model=schemas.Post, status_code=status.HTTP_200_OK)
def get_post(post_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a single post by ID.
    """
    post = crud.get_post(db, post_id=post_id)
    if post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
    return post

@router.put("/{post_id}", response_model=schemas.Post, status_code=status.HTTP_200_OK)
def update_post(post_id: int, post: schemas.PostUpdate, db: Session = Depends(get_db)):
    """
    Update a single post by ID.
    """
    post_db = crud.get_post(db, post_id=post_id)
    if post_db is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
    return crud.update_post(db=db, post_id=post_id, post=post)

@router.delete("/{post_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(post_id: int, db: Session = Depends(get_db)):
    """
    Delete a single post by ID.
    """
    post_db = crud.get_post(db, post_id=post_id)
    if post_db is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
    crud.delete_post(db=db, post_id=post_id)
    return {"detail": "Post deleted"}
```
这个文件包含了FastAPI的路由定义和处理函数。每个函数都对应一个HTTP方法（GET、POST、PUT、DELETE），并且都有相应的依赖注入（数据库会话）。此外，还包含了请求/响应模型（使用Pydantic模型定义）、错误处理和状态码，以及符合RESTful API设计原则的文档字符串。