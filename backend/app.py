from fastapi import FastAPI

# FASTAPI
app = FastAPI()


@app.get("/ping")
async def ping():
    return {"test": "acknowledged!"}
