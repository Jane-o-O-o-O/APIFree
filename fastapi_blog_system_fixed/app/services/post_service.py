 ```python
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from loguru import logger
from . import schemas
from .models import Post

class PostService:
    @staticmethod
    def get_posts(db: Session):
        """
        Service for retrieving all posts.

        Args:
            db (Session): The database session.

        Returns:
            list: A list of Post objects.
        """
        try:
            posts = db.query(Post).all()
            return posts
        except SQLAlchemyError as e:
            logger.error(f"Error retrieving posts: {e}")
            raise

    @staticmethod
    def create_post(db: Session, post: schemas.PostCreate):
        """
        Service for creating a new post.

        Args:
            db (Session): The database session.
            post (schemas.PostCreate): The post data to create.

        Returns:
            Post: The created Post object.
        """
        try:
            db_post = Post(title=post.title, content=post.content)
            db.add(db_post)
            db.commit()
            db.refresh(db_post)
            return db_post
        except SQLAlchemyError as e:
            logger.error(f"Error creating post: {e}")
            raise

    @staticmethod
    def get_post(db: Session, post_id: int):
        """
        Service for retrieving a single post by ID.

        Args:
            db (Session): The database session.
            post_id (int): The post ID to retrieve.

        Returns:
            Post: The Post object.
        """
        try:
            post = db.query(Post).filter(Post.id == post_id).first()
            if post is None:
                logger.error(f"Post with ID {post_id} not found")
                raise ValueError(f"Post with ID {post_id} not found")
            return post
        except SQLAlchemyError as e:
            logger.error(f"Error retrieving post: {e}")
            raise

    @staticmethod
    def update_post(db: Session, post_id: int, post: schemas.PostUpdate):
        """
        Service for updating a single post by ID.

        Args:
            db (Session): The database session.
            post_id (int): The post ID to update.
            post (schemas.PostUpdate): The post data to update.

        Returns:
            Post: The updated Post object.
        """
        try:
            db_post = db.query(Post).filter(Post.id == post_id).first()
            if db_post is None:
                logger.error(f"Post with ID {post_id} not found")
                raise ValueError(f"Post with ID {post_id} not found")
            db_post.title = post.title
            db_post.content = post.content
            db.commit()
            db.refresh(db_post)
            return db_post
        except SQLAlchemyError as e:
            logger.error(f"Error updating post: {e}")
            raise

    @staticmethod
    def delete_post(db: Session, post_id: int):
        """
        Service for deleting a single post by ID.

        Args:
            db (Session): The database session.
            post_id (int): The post ID to delete.

        Returns:
            None
        """
        try:
            db_post = db.query(Post).filter(Post.id == post_id).first()
            if db_post is None:
                logger.error(f"Post with ID {post_id} not found")
                raise ValueError(f"Post with ID {post_id} not found")
            db.delete(db_post)
            db.commit()
        except SQLAlchemyError as e:
            logger.error(f"Error deleting post: {e}")
            raise
```

This Python file defines a `PostService` class with methods to retrieve, create, update, and delete posts from a database using SQLAlchemy. Each method includes exception handling, logging, and transaction management to ensure robustness and reliability.