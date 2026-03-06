from fastapi import APIRouter, Depends, HTTPException
from starlette import status
from starlette.responses import JSONResponse, FileResponse, StreamingResponse

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
    return JSONResponse(status_code=200, content={"detail": "I got your details🦐🦐🦐 ", "deployment_details": get_database(deployment_id)})

@router.put("/deployments/{deployment_id}")
def update_deployment(deployment_id: str, dep: Dep):
    return update_mongodb_name(deployment_id, dep)

@router.delete("/deployments/{deployment_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_deployment(deployment_id: str, username: str):
    if username != get_deployment_username(deployment_id):
        return JSONResponse(status_code=status.HTTP_403_FORBIDDEN, content={"detail": "The username does not match the DB admin information.⛔"})
    delete_mongo_db(deployment_id, username)
    return None




#a non related thing i did after the assignment was over not related to the assignment
#todo configure the path
def pirates_secret_message_audio():
    msg_path = r"C:\Users\niviw\Desktop\matmonRemote\projects\amongusB\pirates-secrete-message.mp3"
    with open(msg_path, mode="rb") as f:
        for line in f.readlines():
            yield line

@router.get("/pirates-secrete-message", response_class=StreamingResponse)
def pirates_secrete_message():
    return StreamingResponse(pirates_secret_message_audio(), media_type="audio/mpeg")

#Things I learned from doing this:
#that \U means something in Unicode and I need to put 'r' before the " so it doesn't raise an error. (also \n and \a does something too)
#that there are file modes and one of them is rb and rb means read in binary and rb+ is read and write in binary.
#I learned that there is a StreamingResponse response type, and it can stream any kind of data(files, audio, video...).
#I learned that yield is like return but unlike return it continues to the next step of the code and doesn't break.


