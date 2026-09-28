from flask import request as FlaskRequest

from src.drivers.interfaces import driver_handler_interface


class Calculator_2: 
    
    def __init__(self, driver_handler: driver_handler_interface):
        self.__driver_handler = driver_handler

    def calculate(self, request: FlaskRequest) -> dict: # pyright: ignore[reportInvalidTypeForm]
        body = request.json
        input_data = self.__validate_body(body)
        calculated_number = self.__process_data(input_data)
        format_response = self.__format_response(calculated_number)
        return format_response
        
        
    def __validate_body(self, body: dict) -> list[float]:
        if "numbers" not in body:
            raise Exception("body mal formatado")
        
        input_data = body["numbers"]
        return input_data
        
    def __process_data(self, input_data: list[float]) -> float:
        
        first_process_result = [(num * 11) ** 0.95 for num in input_data]
        result = self.__driver_handler.standard_derivation(first_process_result)
        return float(1 / result)
    
    def __format_response(self, calculated_number: float) -> dict:
        return {
            "data": {
                "Calculator":2,
                "result": round(calculated_number, 2)
            }
        }