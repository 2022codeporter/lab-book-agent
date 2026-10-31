from fastapi import FastAPI
from app.api import auth, user, files, lab, equipment
from app.database import Base, engine
from fastapi import HTTPException
from starlette.middleware.cors import CORSMiddleware
from fastapi.exceptions import RequestValidationError
from app.common.exceptions import (
    BusinessException,
    bussiness_excpetion_hadler,
    http_excpetion_hadler,
    validation_excpetion_hadler,
    global_excpetion_hadler,
)
from fastapi.staticfiles import StaticFiles
from app.config import UPLOAD_DIR
from app.models.lab import Lab
from app.models.equipment import Equipment


Base.metadata.create_all(bind=engine) # 建表

app = FastAPI()

# 挂载静态资源：/uploads/xxx.jpg → uploads/xxx.jpg
app.mount("/uploads", StaticFiles(directory=UPLOAD_DIR), name="uploads")

# 解决跨域问题
origins = [
	"http://localhost:5173",
	"http://127.0.0.1:5173",
]
app.add_middleware(
	CORSMiddleware,
	allow_origins=origins,        # 允许的前端源，不要直接写 ["*"]
	allow_credentials=True,       # ✅ 关键：允许前端携带 Authorization token
	allow_methods=["*"],          # 允许所有请求方法 GET POST PUT DELETE OPTIONS
	allow_headers=["*"],          # 允许所有请求头（包含Authorization）
)

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
app.include_router(files.router)
app.include_router(lab.router)
app.include_router(equipment.router)



if __name__ == '__main__':
  import uvicorn
  uvicorn.run("main:app", reload=True, host="127.0.0.1", port=8000)