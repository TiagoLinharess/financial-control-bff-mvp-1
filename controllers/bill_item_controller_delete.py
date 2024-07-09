import requests
from flask import jsonify
from schemas import get_default_error, RequestDeleteSchema
from utils import make_login_api_request, make_financial_control_api_request

# Rota de DELETE do endpoint de Bill Items
def delete_bill_items(form: RequestDeleteSchema, session_id: str):
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

        # Body da requisição
        files = {
            "id": (None, form.id)
        }
        
        # Requisição par a api do financial control
        response = make_financial_control_api_request("DELETE", files)

        # Retorno de sucesso da rota
        return response.json()
    except Exception as e:
        # Retorno de erro da rota
        return get_default_error(str(e))