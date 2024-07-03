from flask import jsonify
import requests
from schemas import get_response_login_json, get_default_error, RequestUserSchema

# Rota de Login de usuário POST
def login_post(form: RequestUserSchema):

    # Endpoint de Login da api de login
    url = "http://localhost:3000/login"

    # Payload de Login da api de login
    payload = {
        "email": form.email,
        "password": form.password
    }

    # Request
    response = requests.post(url, payload)

    if response.status_code == 200:
        data = response.json()

        # Retorno de sucesso da rota
        return get_response_login_json(data.get("id"), data.get("refresh_token"))
    elif response.status_code == 400:

        # Retorno de erro da rota
        return get_default_error("Email ou senha incorretos.")
    else:

        # Retorno de erro da rota
        return get_default_error("Não foi possível efetuar o login.")