from fastapi import APIRouter, Depends, HTTPException
from starlette import status
from starlette.responses import JSONResponse

from src.api.actions.mongodb import create_mongo_db, update_mongodb_name
from src.api.actions.postgres import get_database
from src.api.modules.deployment import Dep

router = APIRouter(prefix="/deployments",tags=["items"])


#todo add status code and response
@router.post("/createDB")
def create_db(dep: Dep):
    if len(dep.username) < 3:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={"detail": "Username must be at least 3 characters long"})
    return JSONResponse(status_code=status.HTTP_201_CREATED, content={"detail": "Database created successfully", "id": create_mongo_db(dep.db_name, dep.username)})

@router.get("/deployments/:<deployment_id>")
def get_deployment(deployment_id: str):
    return JSONResponse(status_code=status.HTTP_200_OK, content={"detail": "got your details", "deployment_details": get_database(deployment_id)})

@router.put("/deployments/{deployment_id}")
def update_deployment(deployment_id: str, dep: Dep):
    return update_mongodb_name(deployment_id, dep)