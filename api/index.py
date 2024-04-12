from fastapi import FastAPI

app = FastAPI(docs_url="/api/swagger", redoc_url="/api/redoc")

@app.get("/api/python")
def hello_world():
    return {"message": "Hello World"}