from fastapi import FastAPI
from app.api import auth, user
from app.database import Base, engine
from fastapi import HTTPException
from fastapi.exceptions import RequestValidationError
from app.common.exceptions import (
    BusinessException,
    bussiness_excpetion_hadler,
    http_excpetion_hadler,
    validation_excpetion_hadler,
    global_excpetion_hadler,
)

Base.metadata.create_all(bind=engine)

app = FastAPI()



# 注册异常处理器
app.add_exception_handler(BusinessException, bussiness_excpetion_hadler)
app.add_exception_handler(HTTPException, http_excpetion_hadler)
app.add_exception_handler(RequestValidationError, validation_excpetion_hadler)
app.add_exception_handler(Exception, global_excpetion_hadler)



@app.get("/")
def root():
  return {"message": "我是Fastapi"}



app.include_router(auth.router)
app.include_router(user.router)



if __name__ == '__main__':
  import uvicorn
  uvicorn.run("main:app", reload=True, host="127.0.0.1", port=8000)