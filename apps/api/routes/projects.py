"""
SONIQ MASTER AI
Project management routes.
"""

from uuid import uuid4

from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(
    prefix="/projects",
    tags=["Projects"],
)


class ProjectCreate(BaseModel):
    name: str
    description: str = ""


projects = []


@router.post("/")
async def create_project(project: ProjectCreate):
    """
    Create a new mastering project.
    """

    new_project = {
        "id": uuid4().hex,
        "name": project.name,
        "description": project.description,
        "status": "created",
    }

    projects.append(new_project)

    return {
        "status": "success",
        "project": new_project,
    }


@router.get("/")
async def get_projects():
    """
    Return all mastering projects.
    """

    return {
        "status": "success",
        "projects": projects,
    }
