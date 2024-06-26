from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "From FastAPI! Jenkins CI-CD working, testing polling...."}

@app.get("/hello/{user}")
def say_hello(user: str):
    return {"message": f"Hey there {user}!"}