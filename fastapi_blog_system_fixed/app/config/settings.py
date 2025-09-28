 ```python
from pydantic import BaseSettings, validator
from typing import List, Optional

class Settings(BaseSettings):
    """
    Configuration settings for the application.
    
    Attributes:
        API_KEY (str): The API key for accessing external services.
        API_SECRET (str): The API secret for accessing external services.
        DEBUG (bool): Whether the application is in debug mode.
        DATABASE_URL (str): The URL for the database connection.
        ALLOWED_HOSTS (List[str]): List of allowed hostnames.
        SECRET_KEY (str): The secret key for CSRF protection.
        EMAIL_BACKEND (str): The backend for sending emails.
        EMAIL_HOST (str): The host for sending emails.
        EMAIL_PORT (int): The port for sending emails.
        EMAIL_HOST_USER (str): The username for the email host.
        EMAIL_HOST_PASSWORD (str): The password for the email host.
        EMAIL_USE_TLS (bool): Whether to use TLS for email sending.
    """
    
    API_KEY: str
    API_SECRET: str
    DEBUG: bool = False
    DATABASE_URL: str
    ALLOWED_HOSTS: List[str] = ["localhost", "127.0.0.1"]
    SECRET_KEY: str
    EMAIL_BACKEND: str = "django.core.mail.backends.smtp.EmailBackend"
    EMAIL_HOST: str = "smtp.example.com"
    EMAIL_PORT: int = 587
    EMAIL_HOST_USER: str
    EMAIL_HOST_PASSWORD: str
    EMAIL_USE_TLS: bool = True
    
    @validator("API_KEY", "API_SECRET", "SECRET_KEY", "EMAIL_HOST_USER", "EMAIL_HOST_PASSWORD")
    def not_empty(cls, v):
        if not v:
            raise ValueError("Cannot be empty")
        return v
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        env_prefix = "APP_"

# Example usage:
# from app.config.settings import Settings
# settings = Settings()
# print(settings.API_KEY)
```

### Explanation:
1. **Class Definition**: The `Settings` class inherits from `BaseSettings` provided by Pydantic.
2. **Attributes**: Each attribute represents a configuration setting with a type annotation.
3. **Default Values**: Default values are provided for some attributes, such as `DEBUG` and `ALLOWED_HOSTS`.
4. **Environment Variables**: The `env_file` attribute specifies the path to the `.env` file, and `env_file_encoding` specifies the encoding of the file. The `env_prefix` ensures that environment variables are prefixed with `APP_`.
5. **Validation**: The `not_empty` validator ensures that certain attributes are not empty.
6. **Documentation**: The class and attribute docstrings provide documentation for the configuration settings.

This configuration file allows for easy management of application settings, with clear validation and default values, and supports different environments through environment variables.