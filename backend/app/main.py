from fastapi import FastAPI

from app.api import auth
from app.database import Base, engine
from app.models.user import User

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth.router)

@app.get("/")
def root():
  return {"message": "我是Fastapi"}







if __name__ == '__main__':
  import uvicorn
  uvicorn.run("main:app", reload=True, host="127.0.0.1", port=8000)