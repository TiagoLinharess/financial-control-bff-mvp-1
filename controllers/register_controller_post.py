from schemas import get_default_success_with_message, get_default_error, RequestUserSchema
from utils import make_login_api_request

# Rota de Registro de usuário POST
def register_post(form: RequestUserSchema):
    try:
        # Payload de registro da api de login
        payload = {
            "email": form.email,
            "password": form.password
        }

        # Request
        response = make_login_api_request("/register", payload)

        if response.status_code == 201:

            # Retorno de sucesso da rota
            return get_default_success_with_message("success", 201)
        else:
            data = response.json()

            # Retorno de erro da rota
            return get_default_error(data.get("error"))
    except Exception as e:
        # Retorno de erro da rota
        return get_default_error(str(e))

