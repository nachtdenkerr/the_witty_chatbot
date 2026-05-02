from fastapi import FastAPI
from the_witty_senior.app.routes.tutor import router

app = FastAPI()
app.include_router(router)
