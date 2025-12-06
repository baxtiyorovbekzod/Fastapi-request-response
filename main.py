from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Leo Messi GOAT"}

@app.get("/home")
async def home():
    return {"message": "Salom Dunyo"}


# url: http://127.0.0.1:8000/
# url: http://127.0.0.1:8000/home
