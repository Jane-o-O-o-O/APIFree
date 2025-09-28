 ```python
# app/schemas/user.py
from pydantic import BaseModel, EmailStr, Field, validator
from typing import Optional

class UserBase(BaseModel):
    """
    Base schema for User.
    """
    username: str = Field(..., min_length=3, max_length=50)
    email: EmailStr
    full_name: Optional[str] = Field(None, min_length=1, max_length=100)

    class Config:
        orm_mode = True

class UserCreate(UserBase):
    """
    Schema for creating a new User.
    """
    password: str = Field(..., min_length=8, max_length=100)

    @validator('password')
    def validate_password(cls, v):
        if not any(char.isdigit() for char in v):
            raise ValueError('Password must contain at least one digit')
        if not any(char.isupper() for char in v):
            raise ValueError('Password must contain at least one uppercase letter')
        if not any(char.islower() for char in v):
            raise ValueError('Password must contain at least one lowercase letter')
        return v

class UserUpdate(UserBase):
    """
    Schema for updating an existing User.
    """
    password: Optional[str] = Field(None, min_length=8, max_length=100)

    @validator('password', pre=True, always=True)
    def validate_password(cls, v):
        if v is None:
            return v
        if not any(char.isdigit() for char in v):
            raise ValueError('Password must contain at least one digit')
        if not any(char.isupper() for char in v):
            raise ValueError('Password must contain at least one uppercase letter')
        if not any(char.islower() for char in v):
            raise ValueError('Password must contain at least one lowercase letter')
        return v

class User(UserBase):
    """
    Full schema for a User.
    """
    id: int
    hashed_password: str

    class Config:
        orm_mode = True

# Example data
user_example = {
    "username": "john_doe",
    "email": "john.doe@example.com",
    "full_name": "John Doe",
    "password": "P@ssw0rd"
}

user_create_example = {
    "username": "jane_doe",
    "email": "jane.doe@example.com",
    "full_name": "Jane Doe",
    "password": "P@ssw0rd"
}

user_update_example = {
    "username": "jane_doe",
    "email": "jane.doe@example.com",
    "full_name": "Jane Doe",
    "password": "NewP@ssw0rd"
}
```

This file defines the necessary Pydantic models for a User, including `UserBase`, `UserCreate`, `UserUpdate`, and `User`. Each class includes validation and serialization logic, as well as a `Config` class for ORM mode. Additionally, example data is provided for each model.