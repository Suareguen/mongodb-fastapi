from fastapi import FastAPI
from app.api.endpoints import items

app = FastAPI()

# Include the item API routes
app.include_router(items.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)
