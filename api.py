from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from Firebase import GetQuestions, GetAnswers

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/{data}")
async def read_item(data):
    if type(data) is str:
        if data == "questions":
            return GetQuestions()
        if data == "answers":
            return GetAnswers()

@app.get("/")
async def root():
    return {"message": "Hello World"}
