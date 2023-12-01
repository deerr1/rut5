from pydantic import BaseModel
from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse
import uvicorn

from db.database import engine, Base
from routes import rut

Base.metadata.create_all(bind=engine)

app = FastAPI()
routes = APIRouter()

routes.include_router(rut.router)

app.include_router(routes, prefix="/project")

@app.get("/", include_in_schema=False)
def docs_redirect():
    return RedirectResponse(f"/docs")


origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True, access_log=False)