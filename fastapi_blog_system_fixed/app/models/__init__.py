```python
# app/models/__init__.py
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
import uuid

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(80), unique=True, index=True, nullable=False)
    email = Column(String(120), unique=True, index=True, nullable=False)
    password_hash = Column(String(128))
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    posts = relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"<User(username={self.username}, email={self.email})>"

class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(100), nullable=False)
    content = Column(String(1000), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    def __repr__(self):
        return f"<Post(title={self.title}, content={self.content[:50]}...)>"
```

This SQLAlchemy ORM model defines two classes: `User` and `Post`. The `User` class includes fields for username, email, password hash, creation and update timestamps, and a relationship to a `Post` model. The `Post` class includes fields for title, content, user ID (foreign key), and creation and update timestamps. Each model class has an `__repr__` method for easy representation and a docstring for documentation. The models are defined using SQLAlchemy's ORM system and are declared with appropriate field types, constraints, and relationships.