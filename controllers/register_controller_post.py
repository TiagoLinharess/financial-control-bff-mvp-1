import requests
from schemas import get_default_success_with_message, get_default_error, RequestUserSchema

# Rota de Registro de usuário POST
def register_post(form: RequestUserSchema):

    # Endpoint de registro da api de login
    url = "http://localhost:3000/register"

    # Payload de registro da api de login
    payload = {
        "email": form.email,
        "password": form.password
    }

    # Request
    response = requests.post(url, payload)

    if response.status_code == 201:

        # Retorno de sucesso da rota
        return get_default_success_with_message("Usuário criado com o email " + form.email, 201)
    elif response.status_code == 400:

        # Retorno de erro da rota
        return get_default_error("O email inserido ja está sendo usado")
    else:

        # Retorno de erro da rota
        return get_default_error("Não foi possível criar usuário")
