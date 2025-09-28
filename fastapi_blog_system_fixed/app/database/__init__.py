 ```python
# app/database/__init__.py

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.exc import SQLAlchemyError

class DatabaseConnection:
    """
    A class to manage database connections using SQLAlchemy.
    """

    def __init__(self, db_url):
        """
        Initialize the database connection.

        Args:
            db_url (str): The SQLAlchemy database URL.
        """
        self.engine = create_engine(db_url, pool_size=10, max_overflow=20)
        self.session_factory = scoped_session(sessionmaker(bind=self.engine))

    def get_session(self):
        """
        Get a database session.

        Returns:
            sqlalchemy.orm.Session: A database session.
        """
        return self.session_factory()

    def close_session(self):
        """
        Close the database session.
        """
        self.session_factory.remove()

    def execute_query(self, query, *args, **kwargs):
        """
        Execute a database query.

        Args:
            query (str): The SQL query to execute.
            *args: Positional arguments to pass to the query.
            **kwargs: Keyword arguments to pass to the query.

        Returns:
            list: The result of the query.
        """
        session = self.get_session()
        try:
            result = session.execute(query, *args, **kwargs)
            session.commit()
            return result.fetchall()
        except SQLAlchemyError as e:
            session.rollback()
            raise e
        finally:
            self.close_session()

# Usage example
if __name__ == "__main__":
    db_url = os.getenv("DATABASE_URL", "sqlite:///example.db")
    db = DatabaseConnection(db_url)
    result = db.execute_query("SELECT * FROM example_table")
    print(result)
```

This file defines a `DatabaseConnection` class that manages database connections using SQLAlchemy. It includes methods for getting and closing sessions, executing queries, and handling errors. The class uses a connection pool to manage database connections efficiently. The `__init__` method initializes the database engine and session factory, while the `get_session` and `close_session` methods provide a way to manage the session lifecycle. The `execute_query` method allows executing SQL queries safely and handling exceptions.