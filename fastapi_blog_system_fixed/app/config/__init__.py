 ```python
# app/config/__init__.py
from pydantic import BaseSettings, Field
from dotenv import load_dotenv
import os

class Settings(BaseSettings):
    """
    Configuration settings for the application.

    Attributes:
        API_URL (str): The URL of the API.
        API_KEY (str): The API key for authentication.
        DATABASE_URL (str): The URL of the database.
        DEBUG (bool): Whether the application is in debug mode.
        SECRET_KEY (str): The secret key for cryptographic operations.
        MAX_RETRIES (int): The maximum number of retries for failed operations.
        TIMEOUT (int): The timeout duration in seconds for network requests.

    Environment Variables:
        API_URL: The URL of the API.
        API_KEY: The API key for authentication.
        DATABASE_URL: The URL of the database.
        DEBUG: Whether the application is in debug mode.
        SECRET_KEY: The secret key for cryptographic operations.
        MAX_RETRIES: The maximum number of retries for failed operations.
        TIMEOUT: The timeout duration in seconds for network requests.
    """
    API_URL: str = Field(..., env='API_URL')
    API_KEY: str = Field(..., env='API_KEY')
    DATABASE_URL: str = Field(..., env='DATABASE_URL')
    DEBUG: bool = Field(False, env='DEBUG')
    SECRET_KEY: str = Field(..., env='SECRET_KEY')
    MAX_RETRIES: int = Field(3, env='MAX_RETRIES')
    TIMEOUT: int = Field(10, env='TIMEOUT')

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

# Load environment variables from .env file
load_dotenv()

# Create an instance of the settings
settings = Settings()
```

### Explanation:
1. **Pydantic Settings**: The `Settings` class inherits from `BaseSettings` and uses Pydantic to define and validate the configuration settings.
2. **Environment Variables**: Each attribute in the `Settings` class is annotated with `Field` and has a default value that is read from an environment variable using the `env` parameter.
3. **Configuration Validation**: Pydantic automatically validates the types of the configuration values.
4. **Default Values**: Default values are provided for some attributes if they are not set in the environment variables.
5. **Support Different Environments**: The `env_file` parameter in the `Config` class specifies the path to the `.env` file, which can be different for different environments (e.g., `.env.development`, `.env.production`).
6. **Configuration Documentation**: The docstring for the `Settings` class and each attribute provides a description of the configuration setting.
7. **Load Environment Variables**: The `load_dotenv()` function from the `dotenv` package is used to load environment variables from a `.env` file.

This configuration file sets up a robust and flexible way to manage application settings using Pydantic, with support for environment variables, validation, and default values.