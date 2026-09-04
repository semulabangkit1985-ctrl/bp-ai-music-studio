from pydantic import BaseModel, EmailStr, Field

class RegisterIn(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8)

class LoginIn(BaseModel):
    email: EmailStr
    password: str

class MasterIn(BaseModel):
    audio_id: int
    style: str = "Natural"

class JobOut(BaseModel):
    id: int
    status: str
    output_path: str | None = None
    report: dict | None = None
