# with using the mogodb atlas database....
from fastapi import FastAPI,HTTPException

# now connecting this api to the mongodb atlas database
from pydantic import BaseModel
from pymongo import MongoClient




app=FastAPI()



# here i have defined two list named movie name and movie year globally.
movie_name=['Inception','Dark Knight','Avengers','Monkey Temple','Leo','Baka2']
movie_year=[2010,2022,2011,2009,2025,2022]

# combining this both list of  into a dictionary
movies=[{"title":name,"year":year} for name,year in zip(movie_name,movie_year)]

@app.get("/")
async def read_root():
    return {"Message": "This api gonne be used to connect to the mongodb atlas"}

#this will simply get or list all the movies.
@app.get("/films")
def get_movies():
 return movies

#this will get a single movie
@app.get("/film/{film_id}")
def get_single_movie(film_id: int):
    
    if film_id<1 or film_id>len(movies):
        raise HTTPException(status_code=404,detail="Movie not found")
    return movies[film_id-1]

#this will delete the movie
@app.delete("/film/{film_id}")
def delete_movie(film_id: int):
    if film_id<1 or film_id>len(movies):
        raise HTTPException(status_code=404,detail="Movie not found")
    del_movie=movies.pop(film_id-1)
    return {"message":f"Movie {del_movie['title']} has been deleted"}

#this will add the movie
@app.post("/film")
def add_movie(movie:dict):
    movies.append(movie)
    return {"message":f"Movie {movie['title']} has been added"}


#this will update the movie
@app.put("/film/{film_id}")
def update_movie(film_id: int,movie:dict):
    if film_id<1 or film_id>len(movies):
        raise HTTPException(status_code=404,detail="Invalid movie id")
    movies[film_id-1].update(movie) # update the movie
    return {"message":f"Movie {movie['title']} has been updated"}