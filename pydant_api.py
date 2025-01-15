# This api is connecting to the mysql database server... with using the pydantic models

from fastapi import FastAPI,HTTPException
import mysql.connector
from pydantic import BaseModel
from importfiles import movies

app=FastAPI()

# connecting to the database
mydb=mysql.connector.connect(host="localhost",user="root",password="",database="movies") # here database name is movies but the table name in the database is films

# creating a cursor object
mycursor=mydb.cursor()

@app.get("/")
async def read_root():
    return {"Hello": "World"}

#this will simply get or list all the movies.
@app.get("/films")
def get_movies():

    # getting all the movies using sql query
    sql="select * from Films" # here Films is the table name in the database called movies 
    mycursor.execute(sql)
    movies=mycursor.fetchall()

    # this will return all the movies 
    return movies

#this will get a single movie by id
@app.get("/film/{film_id}")
def get_single_movie(film_id: int):
    
    # getting a single film name using the id in the sql query
    sql="select * from Films where id=%s" # here Films is the table name in
    # the database called movies and id is the id of the movie
    val=(film_id,)
    mycursor.execute(sql,val)
    movies=mycursor.fetchall()
    return movies[0]

# this will get a single movie name by title
@app.get("/film_title/{film_title}")
def get_single_movie_by_title(film_title: str):
    # getting a single film name using the title in the sql query
    sql="select * from Films where title=%s" # here Films is the table name
    # in the database called movies and title is the title of the movie
    val=(film_title,)
    mycursor.execute(sql,val)
    movie=mycursor.fetchall()

    if not len(movie):
        return HTTPException(status_code=404,detail="Sorry! The title you have provided is not in the database")
    return movie[0]

#this will add the movie
@app.post("/film")
def add_movie(movie:movies):

    # adding the movie to the database
    sql="insert into Films(title,year,storyline) values(%s,%s,%s)"
    val=(movie.title,movie.year,movie.storyline)
    mycursor.execute(sql,val)
    mydb.commit()
    return movie

# this will update the movie using the film_id
@app.put("/film/{film_id}")
def update_movie(movie:movies,film_id:int): # here instead of passing two data we already has passed the dictionary so no need to pass the film_id:int as value
    
    # updating the movie in the database
    sql="update Films set title=%s,year=%s,storyline=%s where id=%s"
    val=(movie.title,movie.year,movie.storyline,film_id)
    mycursor.execute(sql,val)
    mydb.commit()
    return {"message":f"Movie {movie.title} has been updated successfully!!"} 

#this will delete the movie using film_id
@app.delete("/film/{film_id}")
def delete_movie(film_id: int):
    # deleting a movie from the database
    sql="delete from Films where id=%s" # here Films is the table name 
    val=(film_id,)
    mycursor.execute(sql,val)
    mydb.commit()
    return {"Status":"The movie has been deleted successfully!!"}
         

# #this will update the movie
# @app.put("/film/{film_id}")
# def update_movie(film_id: int,movie:dict): #here we are updating the movie with dictionary so no need to passs the film id as we already have defined as dict so on next function i am gonna update the film with id as we already defined the dictionary and it's the best practice...
    
#     # updating the movie in the database
#     sql="update Films set title=%s,year=%s,storyline=%s where id=%s"
#     val=(movie['title'],movie['year'],movie['storyline'],film_id)
#     mycursor.execute(sql,val)
#     mydb.commit()
#     return {"message":f"Movie {movie['title']} has been updated successfully!!"} 

