from pydantic import BaseModel
from typing import List

# Eschemas
class ResponseIncomeSchema(BaseModel):
    id: int = 1
    name: str = "Bill"
    type: str = "income"
    value: float = 100

class ResponseOutcomeSchema(BaseModel):
    id: int = 2
    name: str = "Bill"
    type: str = "saída"
    value: float = 100

class ResponseMonthSchema(BaseModel):
    id: int = 1
    month: str = "april"
    incomes: List[ResponseIncomeSchema]
    outcomes: List[ResponseOutcomeSchema]

class ResponseYearSchema(BaseModel):
    year: str = "2024"
    id: int = 1
    months: List[ResponseMonthSchema]

class ResponseYearsListSchema(BaseModel):
    years: List[ResponseYearSchema]

class ResponseErrorSchema(BaseModel):
    error: str = "Error"

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