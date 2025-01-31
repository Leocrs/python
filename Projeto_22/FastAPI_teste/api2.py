from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn


app = FastAPI()

class inputs(BaseModel):
    input: str
    input2: int

@app.get("/")
def exemplo():
    return {"Olá mundo"}

@app.post("/exemplo2")
def exemplo2(input: inputs):
    return input.input

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
