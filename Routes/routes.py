from fastapi import APIRouter, HTTPException, Query
from Config.db import db
import uuid
from typing import List, Optional
from Models.models import Student  # Import Pydantic model
from fastapi.responses import JSONResponse

# Rename the APIRouter instance to avoid conflict
routes = APIRouter()
collection = db['collection0']


# Create Students
@routes.post("/students")
async def create_student(student: Student):
    try:
        # Generate a custom ID
        id = str(uuid.uuid4())

        # Prepare the document to insert
        student_data = {
            "id": id,  # Custom ID
            "name": student.name,
            "age": student.age,
            "address": {
                "city": student.address.city,
                "country": student.address.country,
            },
        }

        # Insert document into MongoDB
        result = collection.insert_one(student_data)

        # Return the custom ID
        return JSONResponse(status_code=201, content = {"id": id})
        

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# List all Students
@routes.get("/students")
async def list_students(country: Optional[str] = None, age: Optional[int] = Query(None)):
    try:
        # Create a filter dictionary
        filters = {}

        # Filter by country if provided
        if country:
            filters["address.country"] = country

        # Filter by age if provided
        if age is not None:
            filters["age"] = {"$gte": age}  # MongoDB query for "greater than or equal to"

        # Query the MongoDB collection with filters
        students = list(collection.find(filters, {"_id": 0}))  # Exclude MongoDB's default _id field

        return JSONResponse(status_code=200, content = {"students": students})

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Get Student
@routes.get("/students/{id}")
async def get_student(id: str):
    student = collection.find_one({"id": id})
    
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    
    # Return the student document without the internal MongoDB `_id`
    student["_id"] = str(student["_id"])  # Convert _id to string if needed for JSON serialization
    return JSONResponse(status_code=200, content = student)

# Patch Student
@routes.patch("/students/{id}")
async def update_student(id: str, student: Student):
    # Find the student document by id
    existing_student = collection.find_one({"id": id})
    
    if not existing_student:
        raise HTTPException(status_code=404, detail="Student not found")
    
    # Prepare update data
    update_data = {}
    
    if student.name:
        update_data["name"] = student.name
    if student.age:
        update_data["age"] = student.age
    if student.address:
        update_data["address"] = {
            "city": student.address.city,
            "country": student.address.country
        }

    # Update the student in the collection
    result = collection.update_one({"id": id}, {"$set": update_data})
    
    if result.modified_count == 0:
        raise HTTPException(status_code=400, detail="No changes were made")
    
    return JSONResponse(status_code=204, content={})

# Delete Student
@routes.delete("/students/{id}")
async def delete_student(id: str):
    # Find the student document by id
    existing_student = collection.find_one({"id": id})
    
    if not existing_student:
        raise HTTPException(status_code=404, detail="Student not found")
    
    # Delete the student document
    collection.delete_one({"id": id})
    
    return JSONResponse(status_code=200, content={})
