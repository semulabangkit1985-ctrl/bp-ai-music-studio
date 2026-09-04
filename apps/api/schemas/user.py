"""
SONIQ MASTER AI
User-related API schemas.
"""

from pydantic import BaseModel, EmailStr, Field


class UserCreate(BaseModel):
    """
    Schema for creating a new user account.
    """

    email: EmailStr
    password: str = Field(
        ...,
        min_length=8,
        max_length=128,
    )


class UserLogin(BaseModel):
    """
    Schema for user login.
    """

    email: EmailStr
    password: str = Field(
        ...,
        min_length=8,
        max_length=128,
    )


class UserResponse(BaseModel):
    """
    Public user information.
    """

    id: str
    email: EmailStr
    is_active: bool = True


class TokenResponse(BaseModel):
    """
    Authentication token response.
    """

    access_token: str
    token_type: str = "bearer"
