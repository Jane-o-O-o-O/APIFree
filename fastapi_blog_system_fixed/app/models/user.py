```python
# app/models/user.py
from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    """
    SQLAlchemy model for the User entity.
    """
    __tablename__ = 'users'
    __table_args__ = (
        # Add any table-level constraints or indexes here if needed
        # For example:
        # Index('idx_email', 'email', unique=True)
    )

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password_hash = Column(String(120), nullable=False)
    created_at = Column(DateTime, default=func.now())
    last_login = Column(DateTime)

    # Define relationships if necessary
    # For example:
    # orders = relationship("Order", back_populates="user")

    def __repr__(self):
        return f"<User(username={self.username}, email={self.email})>"

# Example of a related model (Order) if needed
# class Order(Base):
#     """
#     SQLAlchemy model for the Order entity.
#     """
#     __tablename__ = 'orders'
#     id = Column(Integer, primary_key=True, index=True)
#     user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
#     order_date = Column(DateTime, default=func.now())
#     total_amount = Column(Float, nullable=False)
#     user = relationship("User", back_populates="orders")
```

请根据实际需求调整字段类型、约束和关系映射。