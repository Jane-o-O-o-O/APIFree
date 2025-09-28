 ```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.exc import SQLAlchemyError

# Database configuration
DATABASE_URL = "postgresql://user:password@localhost/dbname"

# Create an engine with connection pool configuration
engine = create_engine(
    DATABASE_URL,
    pool_size=10,
    max_overflow=20,
    pool_timeout=30,
    pool_recycle=1800,
)

# Create a session factory bound to the engine
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db() -> Session:
    """
    Dependency to get a database session.

    This function creates a new database session using the SQLAlchemy session factory.
    It handles the session management, including committing and closing the session.

    Returns:
        Session: A SQLAlchemy database session.

    Raises:
        SQLAlchemyError: If there is an error during session creation or commit.
    """
    db = SessionLocal()
    try:
        yield db
        db.commit()
    except SQLAlchemyError as e:
        db.rollback()
        raise e
    finally:
        db.close()
```

### Explanation:
1. **Database Configuration**: The `DATABASE_URL` is defined with the necessary connection details.
2. **Engine Creation**: An engine is created using `create_engine` with connection pool settings to manage database connections efficiently.
3. **Session Factory**: `SessionLocal` is created using `sessionmaker` to bind to the engine. This factory will be used to create new sessions.
4. **Dependency Function (`get_db`)**:
   - **Session Management**: The function yields a new database session, commits the transaction, and closes the session.
   - **Error Handling**: It catches any `SQLAlchemyError` during session creation, commit, or rollback, ensuring that the session is properly closed in all cases.
   - **Documentation**: The function includes a docstring that describes its purpose, parameters, return type, and exceptions it can raise.

This setup ensures that the database sessions are managed efficiently with proper connection pooling and error handling.