from pydantic import BaseModel

# Esquemas
class RequestUserSchema(BaseModel):
    email: str
    password: str

class ResponseLoginSchema(BaseModel):
    user_id: str = "xxxxxx"
    session_id: str = "xxxxxx"

class ResponseRegisterSchema(BaseModel):
    message: str = "success"

# Retorno da api de login
def get_response_login_json(user_id: str, session_id: str):
    return { 
        "user_id": user_id,
        "session_id": session_id
    }, 200