from pydantic import BaseModel

class RequestPostSchema(BaseModel):
    user_id: str
    year: str
    month: str
    type: str
    name: str
    value: float

class RequestDeleteSchema(BaseModel):
    id: int

class RequestPutSchema(BaseModel):
    id: int
    type: str
    name: str
    value: float

class RequestGetSchema(BaseModel):
    user_id: str