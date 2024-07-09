from flask import jsonify
from utils import make_login_api_request
from schemas import get_response_login_json, get_default_error, RequestUserSchema

# Rota de Login de usuário POST
def login_post(form: RequestUserSchema):

    # Payload de registro da api de login
    payload = {
        "email": form.email,
        "password": form.password
    }

    # Request
    response = make_login_api_request("/login", payload)

    if response.status_code == 200:
        data = response.json()

        # Retorno de sucesso da rota
        return get_response_login_json(data.get("id"), data.get("refresh_token"))
    else:
        data = response.json()

        # Retorno de erro da rota
        return get_default_error(data.get("error"))