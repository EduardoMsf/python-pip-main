from fastapi import FastAPI, Body, Path, Query
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List

app = FastAPI()

app.title = "My API"
app.version = "0.1.0"


class Movie(BaseModel):
    id: Optional[int] = None
    title: str = Field(min_length=5, max_length=15)
    overview: str = Field(min_length=15, max_length=50)
    year: int = Field(le=2022)
    rating:float = Field(ge=1, le=10)
    category:str = Field(min_length=5, max_length=15)

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "title": "Mi película",
                "overview": "Descripción de la película",
                "year": 2022,
                "rating": 9.8,
                "category" : "Acción"
            }
        }


movies = [
    {
        "id": 1,
        "title": "Avatar",
        "overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        "year": "2009",
        "rating": 7.8,
        "category": "Accion"
    },
    {
        "id": 2,
        "title": "Inception",
        "overview": "Un ladrón que roba secretos corporativos a través del uso de la tecnología de compartir sueños ...",
        "year": "2010",
        "rating": 8.8,
        "category": "Ciencia ficción"
    },
    {
        "id": 3,
        "title": "Interstellar",
        "overview": "Un grupo de exploradores hacen uso de un agujero de gusano recién descubierto para superar las limitaciones en los viajes espaciales humanos ...",
        "year": "2014",
        "rating": 8.6,
        "category": "Aventura"
    },
    {
        "id": 4,
        "title": "The Matrix",
        "overview": "Un programador de computadoras se entera de su verdadera naturaleza como ser en un mundo simulado ...",
        "year": "1999",
        "rating": 8.7,
        "category": "Accion"
    },
    {
        "id": 5,
        "title": "Gladiator",
        "overview": "Un antiguo general romano se propone vengar la corrupción y el asesinato de su familia ...",
        "year": "2000",
        "rating": 8.5,
        "category": "Drama"
    },
    {
        "id": 6,
        "title": "The Dark Knight",
        "overview": "Batman asume la responsabilidad de derrotar a un nuevo y temible criminal conocido como el Joker ...",
        "year": "2008",
        "rating": 9.0,
        "category": "Accion"
    },
    {
        "id": 7,
        "title": "Fight Club",
        "overview": "Un empleado de oficina insomne y un fabricante de jabón carismático forman un club de lucha clandestino ...",
        "year": "1999",
        "rating": 8.8,
        "category": "Drama"
    },
    {
        "id": 8,
        "title": "Pulp Fiction",
        "overview": "Las vidas de dos sicarios de la mafia, un boxeador, un gánster y su esposa, y un par de bandidos dinerarios se entrelazan en cuatro historias de violencia y redención ...",
        "year": "1994",
        "rating": 8.9,
        "category": "Crimen"
    },
    {
        "id": 9,
        "title": "Forrest Gump",
        "overview": "La historia de un hombre con un coeficiente intelectual bajo pero de buen corazón y sus extraordinarias aventuras a lo largo de su vida ...",
        "year": "1994",
        "rating": 8.8,
        "category": "Drama"
    },
]

@app.get("/", tags=["Home"])
def message():
    return HTMLResponse(content="<h1>Apoko si? Desde fastapi</h1>")

@app.get("/movies", tags=["Movies"], response_model=List[Movie], status_code=200)
def get_movies() -> List[Movie]:
    return JSONResponse(content=movies, status_code=200)

@app.get("/movies/{id}", tags=["Movies"], response_model=Movie, status_code=200)
def get_movie(id: int=Path(ge=1, le=2000)) -> Movie:
    for movie in movies:
        if movie["id"] == id:
            return JSONResponse(content=movie, status_code=200)
    return JSONResponse(content={"error": "Movie not found"}, status_code=404)

@app.get("/movies/", tags=["Movies"], response_model=List[Movie], status_code=200)
def get_movies_by_category(category: str =Query(min_length=5, max_length=15 )) -> List[Movie]:
    data = [movie for movie in movies if movie["category"] == category]
    return JSONResponse(content=data, status_code=200)

@app.post("/movies", tags=["Movies"], response_model=dict, status_code=201)
def create_movie(movie: Movie) -> dict:
    movies.append(movie)
    return JSONResponse(content= {'message': 'Se ha registrado correctamente'} , status_code=201)

@app.put("/movies/{id}", tags=["Movies"], response_model=dict, status_code=200)
def update_movie(id: int, movie: Movie) -> dict:
    for i, m in enumerate(movies):
        if m["id"] == id:
            movies[i] = movie
            print(i)
            print(m)
            return JSONResponse(content= {'message': 'Se ha modificado correctamente'} , status_code=200)
    return JSONResponse(content= {'message': 'Error al modificar'}, status_code=404 )

@app.delete("/movies/{id}", tags=["Movies"], response_model=dict, status_code=200)
def delete_movie(id: int) -> dict:
    for i, movie in enumerate(movies):
        if movie["id"] == id:
            del movies[i]
            return JSONResponse(content= {'message': 'Se ha eliminado correctamente'}, status_code=200 )
    return JSONResponse(content= {'message': 'Error al eliminar'}, status_code=404 )