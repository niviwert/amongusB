from fastapi import APIRouter, Depends, HTTPException
from starlette import status
from starlette.responses import JSONResponse

from src.api.actions.mongodb import create_mongo_db, update_mongodb_name, delete_mongo_db
from src.api.actions.postgres import get_database, get_deployment_username
from src.api.modules.deployment import Dep

router = APIRouter(prefix="/deployments",tags=["items"])


#todo add status code and response
@router.post("/createDB")
def create_db(dep: Dep):
    if len(dep.username) < 3:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={"detail": "Username must be at least 3 characters long... YOU ARE TOO SHORT!🤏"})
    return JSONResponse(status_code=status.HTTP_201_CREATED, content={"detail": "Database created successfully", "id": create_mongo_db(dep.db_name, dep.username)})

@router.get("/deployments/{deployment_id}")
def get_deployment(deployment_id: str):
    return JSONResponse(status_code=200, content={"detail": "I got your details🦐🦐🦐", "deployment_details": get_database(deployment_id)})

@router.put("/deployments/{deployment_id}")
def update_deployment(deployment_id: str, dep: Dep):
    return update_mongodb_name(deployment_id, dep)

@router.delete("/deployments/{deployment_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_deployment(deployment_id: str, username: str):
    if username != get_deployment_username(deployment_id):
        return JSONResponse(status_code=status.HTTP_403_FORBIDDEN, content={"detail": "The username does not match the DB admin information.⛔"})
    delete_mongo_db(deployment_id, username)
    return None
