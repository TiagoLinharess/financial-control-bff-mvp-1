from pydantic import BaseModel

class RequestUserSchema(BaseModel):
    email: str
    password: str

class ResponseLoginSchema(BaseModel):
    user_id: str = "xxxxxx"
    session_id: str = "xxxxxx"

class ResponseRegisterSchema(BaseModel):
    message: str = "Usuário criado com o email a@a.com"