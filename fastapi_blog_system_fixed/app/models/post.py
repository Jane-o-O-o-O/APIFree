```python
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Post(Base):
    """
    SQLAlchemy model for the Post entity.
    Represents a blog post with various attributes such as title, content, author, and creation timestamp.
    """

    __tablename__ = 'posts'
    __table_args__ = (
        # Add any additional table arguments here, such as indexes or constraints
        {'mysql_engine': 'InnoDB', 'mysql_charset': 'utf8mb4'}
    )

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(255), nullable=False, index=True)
    content = Column(Text, nullable=False)
    author_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    # Relationship mapping
    author = relationship('User', back_populates='posts')

    def __repr__(self):
        return f"<Post(id={self.id}, title={self.title}, created_at={self.created_at})>"
```

This code snippet defines a SQLAlchemy model for a blog post (`Post`). It includes fields for the post's ID, title, content, author ID, creation timestamp, and update timestamp. The `author_id` field establishes a foreign key relationship with the `User` model, assuming the existence of such a model. The `__repr__` method provides a string representation of the `Post` instances, which is useful for debugging and logging. The `__table_args__` includes table arguments for setting the MySQL engine and charset, although these are specific to MySQL and may not be necessary for other database backends.