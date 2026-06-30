from pydantic import BaseModel, Field
from typing_extensions import Optional



class BookRequest(BaseModel):
    id: Optional[int] = Field(gt=0, default=None)
    title: str = Field(min_length=4, max_length=50)
    author: str = Field(min_length=4, max_length=50)

    model_config = {
        "json_schema_extra": {
            "example": {"title": "Atomic habits", "author": "James Clear"}
        }
    }
