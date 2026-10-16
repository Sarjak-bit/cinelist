from fastapi import FastAPI, HTTPException
from schema import movieCreate, movieView 


app = FastAPI()

movies: list[dict] = [
    {
        "id": 1,
        "title": "Inception",
        "genre": "Sci-Fi",
        "year": 2010,
        "status": "watched",
        "rating": 9,
    },
    {
        "id": 2,
        "title": "Interstellar",
        "genre": "Sci-Fi",
        "year": 2014,
        "status": "planned",
        "rating": None,
    },
]
@app.get("/movies")
def create_movies(movie: movieCreate):
    new_id = max(m["id"] for m in movies) + 1 if movies else id
    
    new_movie = {
        "id": new_id,
        "title": movie.title,
        "genre": movie.genre,
        "year": movie.year,
        "status": movie.status,
        "rating": movie.rating 
        
    }