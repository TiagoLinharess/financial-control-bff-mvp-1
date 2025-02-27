from flask_openapi3 import OpenAPI, Info, Tag
from flask_cors import CORS
from flask import redirect, request

from controllers import register_post, login_post, get_bill_items, post_bill_items, update_bill_items, delete_bill_items

from schemas import ResponseSuccessSchema, ResponseErrorSchema, ResponseLoginSchema, ResponseRegisterSchema, RequestUserSchema, RequestGetSchema, ResponseYearsListSchema, RequestPostSchema, RequestDeleteSchema, RequestPutSchema

# Inicializa API
info = Info(title="Financial Control BFF API MVP 1", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# Documentação
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
@app.get('/', tags=[home_tag])
def home():
    return redirect('/openapi')

# Rota Registro POST
post_register_tag = Tag(name="Registrar usuário", description="Cria usuário com email e senha.")
@app.post('/register', tags=[post_register_tag], responses={"201": ResponseRegisterSchema, "400": ResponseErrorSchema})
def register(form: RequestUserSchema):
    return register_post(form)

# Rota Login POST
post_register_tag = Tag(name="Login usuário", description="Efetua login do usuário com email e senha.")
@app.post('/login', tags=[post_register_tag], responses={"200": ResponseLoginSchema, "400": ResponseErrorSchema})
def login(form: RequestUserSchema):
    return login_post(form)

# Rota buscar Item GET
get_bill_items_tag = Tag(name="Buscar items por usuário", description="Procuras os items do usuário agrupados por meses e anos.")
@app.get('/bill_items', tags=[get_bill_items_tag], responses={"200": ResponseYearsListSchema, "400": ResponseErrorSchema})
def get(query: RequestGetSchema):
    return get_bill_items(query, request.headers.get("session_id"))

# Rota criação de Item POST
post_register_tag = Tag(name="Criar Item", description="Cria item agrupado por mês e ano.")
@app.post('/bill_items', tags=[post_register_tag], responses={"200": ResponseSuccessSchema, "400": ResponseErrorSchema})
def post(form: RequestPostSchema):
    return post_bill_items(form, request.headers.get("session_id"))

# Rota editar item PUT
put_bill_items_tag = Tag(name="Editar item", description="Edita item já criado.")
@app.put('/bill_items', tags=[put_bill_items_tag], responses={"200": ResponseSuccessSchema, "400": ResponseErrorSchema})
def put(form: RequestPutSchema):
    return update_bill_items(form, request.headers.get("session_id"))

# Rota deletar item DELETE
delete_bill_items_tag = Tag(name="Deletar item", description="Deleta item já criado.")
@app.delete('/bill_items', tags=[delete_bill_items_tag], responses={"200": ResponseSuccessSchema, "400": ResponseErrorSchema})
def delete(form: RequestDeleteSchema):
    return delete_bill_items(form, request.headers.get("session_id"))