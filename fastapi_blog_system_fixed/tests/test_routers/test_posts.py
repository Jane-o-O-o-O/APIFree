```python
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from sqlalchemy.orm import Session
from typing import List
from tests.test_routers.database import SessionLocal, engine, Base
from tests.test_routers.models import Post

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Request/Response Models
class PostBase(BaseModel):
    title: str
    content: str

class PostCreate(PostBase):
    pass

class Post(PostBase):
    id: int

    class Config:
        orm_mode = True

# Database Models
Base.metadata.create_all(bind=engine)

# CRUD Operations
def get_posts(db: Session):
    return db.query(Post).all()

def create_post(db: Session, post: PostCreate):
    db_post = Post(**post.dict())
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

def get_post(db: Session, post_id: int):
    return db.query(Post).filter(Post.id == post_id).first()

def update_post(db: Session, post_id: int, post: PostCreate):
    db_post = db.query(Post).filter(Post.id == post_id).first()
    if db_post:
        db_post.title = post.title
        db_post.content = post.content
        db.commit()
        db.refresh(db_post)
        return db_post
    else:
        raise HTTPException(status_code=404, detail="Post not found")

def delete_post(db: Session, post_id: int):
    db_post = db.query(Post).filter(Post.id == post_id).first()
    if db_post:
        db.delete(db_post)
        db.commit()
        return JSONResponse(content={"message": "Post deleted successfully"}, status_code=status.HTTP_204_NO_CONTENT)
    else:
        raise HTTPException(status_code=404, detail="Post not found")

# API Routes
@app.get("/posts/", response_model=List[Post], tags=["posts"])
def read_posts(db: Session = Depends(get_db)):
    """
    Get all posts.
    """
    posts = get_posts(db)
    return posts

@app.post("/posts/", response_model=Post, status_code=status.HTTP_201_CREATED, tags=["posts"])
def create_new_post(post: PostCreate, db: Session = Depends(get_db)):
    """
    Create a new post.
    """
    db_post = create_post(db, post)
    return db_post

@app.get("/posts/{post_id}", response_model=Post, tags=["posts"])
def read_post(post_id: int, db: Session = Depends(get_db)):
    """
    Get a single post by ID.
    """
    post = get_post(db, post_id)
    if post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return post

@app.put("/posts/{post_id}", response_model=Post, tags=["posts"])
def update_post_route(post_id: int, post: PostCreate, db: Session = Depends(get_db)):
    """
    Update a single post by ID.
    """
    updated_post = update_post(db, post_id, post)
    if updated_post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return updated_post

@app.delete("/posts/{post_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["posts"])
def delete_post_route(post_id: int, db: Session = Depends(get_db)):
    """
    Delete a single post by ID.
    """
    deleted_post = delete_post(db, post_id)
    if deleted_post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return deleted_post
```

这个文件包含了完整的FastAPI路由实现，包括依赖注入、数据库会话、请求/响应模型、错误处理和状态码，以及RESTful API设计原则。