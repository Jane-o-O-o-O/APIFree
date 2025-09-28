```python
from pydantic import BaseSettings, Field, validator
from typing import Optional
import os

class Config(BaseSettings):
    """Configuration settings for database migrations."""

    SQLALCHEMY_DATABASE_URL: str = Field(..., description="Database URL for SQLAlchemy")
    SQLALCHEMY_MIGRATE_REPO: str = Field(..., description="Path to the migration repository")
    SQLALCHEMY_ECHO: bool = Field(False, description="Enable SQL statement logging")
    ENVIRONMENT: str = Field("development", description="Current environment (development, production, testing)")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

    @validator("SQLALCHEMY_DATABASE_URL")
    def check_database_url(cls, v):
        """Ensure the database URL is valid."""
        if not v.startswith("sqlite:///") and not v.startswith("postgresql://"):
            raise ValueError("Database URL must be a valid PostgreSQL or SQLite URL")
        return v

    @validator("SQLALCHEMY_MIGRATE_REPO")
    def check_migration_repo_path(cls, v):
        """Ensure the migration repository path exists."""
        if not os.path.exists(v):
            raise ValueError("Migration repository path does not exist")
        return v

def run_migrations_offline():
    """
    Function to run migrations offline.

    This function is responsible for running database migrations without an active database connection.
    It uses the settings defined in the Config class to configure the migration process.
    """
    config = Config()
    # Implement migration logic here using SQLAlechmy's command line tools or similar

def run_migrations_online():
    """
    Function to run migrations online.

    This function is responsible for running database migrations with an active database connection.
    It uses the settings defined in the Config class to configure the migration process.
    """
    config = Config()
    # Implement migration logic here using SQLAlchemy's migration engine or similar
```

This Python file defines a `Config` class using Pydantic to manage configuration settings for database migrations. It includes environment variable reading, configuration validation, default values, and support for different environments. The `run_migrations_offline` and `run_migrations_online` functions are placeholders for the actual migration logic, which should be implemented using SQLAlchemy's tools or similar. The file also contains detailed docstrings for each function and class, providing clear documentation and descriptions.