from flask import jsonify
from schemas import RequestGetSchema, get_default_error
from utils import make_login_api_request, make_financial_control_api_request

def get_bill_items(query: RequestGetSchema, session_id: str):
    try:
        # Payload de sessão da api de login
        payload = {
            "refreshToken": session_id
        }

        # Request de sessão para a api de login
        login_response = make_login_api_request("/verify-session", payload)
        login_data = login_response.json()

        # Verfifica se a sessão é válida
        if not login_data.get("is_valid"):
            raise ValueError("Token not valid")

        # Requisição par a api do financial control
        response = make_financial_control_api_request("GET", query.user_id)

        return response.json()
    except Exception as e:
        # Retorno de erro da rota
        return get_default_error(str(e))