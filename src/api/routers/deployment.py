from fastapi import APIRouter, Depends, HTTPException
from starlette import status

from src.api.actions.mongodb import create_mongo_db, update_mongodb_name
from src.api.actions.postgres import get_database
from src.api.modules.deployment import Dep

router = APIRouter(prefix="/deployments",tags=["items"])
@router.post("/createDB", status_code=status.HTTP_201_CREATED)
def create_db(dep: Dep) :
    return create_mongo_db(dep.db_name, dep.username)

@router.get("/deployments/{deployment_id}", status_code=status.HTTP_200_OK)
def get_deployment(deployment_id: str):
    return get_database(deployment_id)

@router.put("/deployments/{deployment_id}", status_code=status.HTTP_200_OK)
def update_deployment(deployment_id: str, dep: Dep):
    return update_mongodb_name(deployment_id, dep)