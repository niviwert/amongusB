import uvicorn
from fastapi import FastAPI, Response
from fastapi.responses import JSONResponse, RedirectResponse

from src.api.actions.mongodb import create_mongo_db
from src.api.routers import deployment

app = FastAPI()
app.include_router(deployment.router)
#@app.post("/createDB")
#def create_db(db_name: str, username: str) :
#    return create_mongo_db(db_name, username)
#
#@app.get("/portal")
#async def get_portal(teleport: bool = False) -> Response:
#    if teleport:
#        return RedirectResponse(url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")
#    return JSONResponse(content={"message": "Here's your interdimensional portal."})


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)