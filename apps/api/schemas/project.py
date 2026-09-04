"""
SONIQ MASTER AI
Project-related API schemas.
"""

from pydantic import BaseModel, Field


class ProjectCreate(BaseModel):
    """
    Schema for creating a mastering project.
    """

    name: str = Field(
        ...,
        min_length=1,
        max_length=200,
    )

    description: str = Field(
        default="",
        max_length=1000,
    )


class ProjectResponse(BaseModel):
    """
    Public project information.
    """

    id: str
    name: str
    description: str = ""
    status: str = "created"


class ProjectListResponse(BaseModel):
    """
    Response containing multiple projects.
    """

    status: str
    projects: list[ProjectResponse]
