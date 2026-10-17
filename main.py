from fastapi import FastAPI, HTTPException, status, Request
from schema import movieCreate, movieView 
from starlette.exceptions import HTTPException as starletteException
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
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
@app.get("/api/movies", 
        response_model= list[movieView])
def get_movies():
    return movies

@app.post("/api/movies", 
        response_model=movieView, 
        status_code= status.HTTP_201_CREATED)
def create_movies(movie: movieCreate):
    new_id = max(m["id"] for m in movies) + 1 if movies else 1
    
    new_movie = {
        "id": new_id,
        "title": movie.title,
        "genre": movie.genre,
        "year": movie.year,
        "status": movie.status,
        "rating": movie.rating 
        
    }
    movies.append(new_movie)
    return new_movie

@app.get("/api/movies/{movie_id}", response_model=movieView)
def get_movie(movie_id: int):
    for movie in movies:
        if movie.get("id") == movie_id:
            return movie
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Movie not found.")


@app.exception_handler(starletteException)
def general_exception_handler(request: Request, exception: starletteException):
    message = (
        exception.detail 
        if exception.detail
        else "An error occurred. Please check you request and try again!!"
    )
    return JSONResponse(
        status_code= exception.status_code,
        content= {
            "detail": message
        }
    )

@app.exception_handler(RequestValidationError)
def validation_exception_handler(request: Request, exception: RequestValidationError):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_CONTENT,
        content= {
            "detail": exception.errors
        }
    )