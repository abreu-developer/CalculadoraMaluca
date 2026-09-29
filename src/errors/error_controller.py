from .http_bad_request_error import HttpBadRequestError
from .http_unprocessable_entity_error import HttpUnprocessableEntityError


def handle_errors(error: Exception) -> dict:
    if isinstance(error, (HttpUnprocessableEntityError, HttpBadRequestError )):
        return{
            "status_code": error.status_code,
            "body":{
                "Errors": [{
                    "title": error.name,
                    "detail":error.message
                }]
            }
        }
    
    return {
            "status_code": 500,
            "body":{
                "Errors": [{
                    "title": "server error",
                    "detail": str(error)
                }]
            }
        }   