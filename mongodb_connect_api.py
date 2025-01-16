from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from pymongo import MongoClient
from bson import ObjectId
from urllib.parse import quote_plus
from typing import List, Optional

app = FastAPI()


# username="nixhell816"
# password="mongo@123"

# encoded_username=quote_plus(username)
# encoded_password=quote_plus(password)

# MongoDB connection
# Replace <db_username> and <db_password> with your actual MongoDB Atlas username and password.
client = MongoClient("mongodb+srv://nixhell816:3W0duaoqG7chmMpR@moviedb.qeg9l.mongodb.net/")
db = client["movies_api"]  # Specify the database name
collection = db["films"]  # Specify the collection name

# Define a Pydantic model for movies
class Movie(BaseModel):
    title: str  # The title of the movie (required)
    year: int  # The release year of the movie (required)
    storyline: str = None  # A brief storyline of the movie (optional)

@app.get("/")
def read_root():
    """
    Root endpoint.
    Returns a simple message to confirm the API is working.
    """
    return {"Message": "This API is connected to MongoDB Atlas."}

@app.get("/films", response_model=list[Movie])
def get_movies():
    """
    Get all movies from the MongoDB collection.
    Excludes the `_id` field for compatibility with the Pydantic model.
    """
    movies = list(collection.find({}, {"_id": 0}))  # Retrieve all movies and exclude `_id`
    return movies

@app.get("/film/{film_id}", response_model=Movie)
def get_single_movie(film_id: str):
    """
    Get a single movie by its ID.
    Converts the string `film_id` to an ObjectId for querying MongoDB.
    If the movie is not found, raises a 404 error.
    """
    try:
        movie = collection.find_one({"_id": ObjectId(film_id)}, {"_id": 0})  # Exclude `_id`
        if not movie:
            raise HTTPException(status_code=404, detail="Movie not found")
        return movie
    except:
        raise HTTPException(status_code=400, detail="Invalid movie ID format")

@app.post("/film", response_model=Movie)
def add_movie(movie: Movie):
    """
    Add a new movie to the MongoDB collection.
    Converts the Pydantic model to a dictionary for insertion into MongoDB.
    """
    movie_dict = movie.model_dump()  # Convert Pydantic model to dictionary
    collection.insert_one(movie_dict)  # Insert into MongoDB
    return movie  # Return the added movie

@app.delete("/film/{film_id}")
def delete_movie(film_id: str):
    """
    Delete a movie by its ID.
    Converts the string `film_id` to an ObjectId for querying MongoDB.
    If the movie is not found, raises a 404 error.
    """
    try:
        result = collection.delete_one({"_id": ObjectId(film_id)})  # Attempt deletion
        if result.deleted_count == 0:
            raise HTTPException(status_code=404, detail="Movie not found")
        return {"message": "Movie successfully deleted."}
    except:
        raise HTTPException(status_code=400, detail="Invalid movie ID format")

@app.put("/film/{film_id}", response_model=Movie)
def update_movie(film_id: str, movie: Movie):
    """
    Update a movie by its ID.
    Converts the string `film_id` to an ObjectId for querying MongoDB.
    Replaces the movie data with the new details from the Pydantic model.
    """
    try:
        movie_dict = movie.model_dump()  # Convert Pydantic model to dictionary
        result = collection.replace_one({"_id": ObjectId(film_id)}, movie_dict)  # Replace document
        if result.matched_count == 0:
            raise HTTPException(status_code=404, detail="Movie not found")
        return movie  # Return the updated movie
    except:
        raise HTTPException(status_code=400, detail="Invalid movie ID format")
