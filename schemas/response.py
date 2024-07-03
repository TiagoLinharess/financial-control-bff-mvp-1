from pydantic import BaseModel

class ResponseErrorSchema(BaseModel):
    error: str = "Ocorreu um erro"

class ResponseSuccessSchema(BaseModel):
    success: bool = True

# Retorno padrão de erro
def get_default_error(exception: str):
    return {
        "error": exception
    }, 400

# Retorno padrão de sucesso
def get_default_success():
    return { "success": True }, 200

# Retorno padrão de sucesso
def get_default_success_with_message(message: str, code: int):
    return { "message": message }, code