from pydantic import BaseModel, Field

class movieBase(BaseModel):
    title: str = Field(min_length=1, max_length=50)
    genre: str
    year: int
    status: str
    rating: int | None = None
    
class movieCreate(movieBase):
    pass

class movieView(movieBase):
    id: int