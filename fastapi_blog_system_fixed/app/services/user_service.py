```python
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from app import schemas
from app.models import User
from app.utils import logger

def get_users(db: Session):
    """
    Service for retrieving all users.

    Args:
    db (Session): The database session.

    Returns:
    List[User]: A list of all users.
    """
    try:
        users = db.query(User).all()
        logger.info(f"Retrieved {len(users)} users")
        return users
    except SQLAlchemyError as e:
        logger.error(f"Failed to retrieve users: {e}")
        raise

def create_user(db: Session, user: schemas.UserCreate):
    """
    Service for creating a new user.

    Args:
    db (Session): The database session.
    user (schemas.UserCreate): The user data to create.

    Returns:
    User: The created user.
    """
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        logger.warning(f"User with email {user.email} already exists")
        raise ValueError("User already exists")
    
    db_user = User(email=user.email, hashed_password=user.hashed_password)
    try:
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        logger.info(f"Created user with ID {db_user.id}")
        return db_user
    except SQLAlchemyError as e:
        db.rollback()
        logger.error(f"Failed to create user: {e}")
        raise

def get_user(db: Session, user_id: int):
    """
    Service for retrieving a single user by ID.

    Args:
    db (Session): The database session.
    user_id (int): The user ID to retrieve.

    Returns:
    User: The retrieved user.
    """
    try:
        user = db.query(User).filter(User.id == user_id).first()
        if not user:
            logger.warning(f"User with ID {user_id} not found")
            raise ValueError("User not found")
        logger.info(f"Retrieved user with ID {user_id}")
        return user
    except SQLAlchemyError as e:
        logger.error(f"Failed to retrieve user: {e}")
        raise

def update_user(db: Session, user_id: int, user: schemas.UserUpdate):
    """
    Service for updating a single user by ID.

    Args:
    db (Session): The database session.
    user_id (int): The user ID to update.
    user (schemas.UserUpdate): The user data to update.

    Returns:
    User: The updated user.
    """
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        logger.warning(f"User with ID {user_id} not found")
        raise ValueError("User not found")
    
    if user.email:
        existing_user = db.query(User).filter(User.email == user.email).first()
        if existing_user and existing_user.id != user_id:
            logger.warning(f"User with email {user.email} already exists")
            raise ValueError("User with this email already exists")

    db_user.email = user.email or db_user.email
    db_user.hashed_password = user.hashed_password or db_user.hashed_password
    try:
        db.commit()
        db.refresh(db_user)
        logger.info(f"Updated user with ID {user_id}")
        return db_user
    except SQLAlchemyError as e:
        db.rollback()
        logger.error(f"Failed to update user: {e}")
        raise

def delete_user(db: Session, user_id: int):
    """
    Service for deleting a single user by ID.

    Args:
    db (Session): The database session.
    user_id (int): The user ID to delete.
    """
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        logger.warning(f"User with ID {user_id} not found")
        raise ValueError("User not found")
    
    try:
        db.delete(db_user)
        db.commit()
        logger.info(f"Deleted user with ID {user_id}")
    except SQLAlchemyError as e:
        db.rollback()
        logger.error(f"Failed to delete user: {e}")
        raise
```

This Python file contains the implementation of the `user_service.py` file, which includes the business logic for user operations such as retrieving, creating, updating, and deleting users. The code also includes database operations, exception handling, data validation, logging, and transaction management. Each function has a detailed docstring explaining its purpose and parameters.