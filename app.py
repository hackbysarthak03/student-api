from fastapi import FastAPI
from Routes.routes import routes  # Import renamed router

app = FastAPI()

# Include the router
app.include_router(routes, prefix="/api", tags=["Students"])

@app.get('/')
async def root():
    return {"message": "Welcome to the API"}
