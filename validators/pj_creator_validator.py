from pydantic import BaseModel, constr, ValidationError
from src.views.http_types.http_request import HttpRequest
from src.errors.errors_types.http_unprocessable_entity import HttpUnprocessableEntity

def pessoa_juridica_creator_validator(http_request: HttpRequest) -> None:
    class BodyData(BaseModel):
        faturamento = float
        idade = int
        nome_fantasia = constr(min_length=1)
        celular = constr(min_length=1)
        email_corporativo = constr(min_length=1)
        categoria = constr(min_length=1)
        saldo = float

    try: 
        BodyData(**http_request.body)

    except ValidationError as e:
        raise HttpUnprocessableEntity(e.errors()) from e
        
