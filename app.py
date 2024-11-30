from fastapi import FastAPI
from Routes.routes import routes  # Import renamed router
import uvicorn
import os

app = FastAPI()

# Include the router
app.include_router(routes, prefix="/api", tags=["Students"])

@app.get('/')
async def root():
    return {"message": "Welcome to the Student API Calls"}

@app.get('/api')
async def root():
    return {"message": "Welcome to the Student API Calls"}


if __name__ == "__main__":
    
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)