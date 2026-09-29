from flask import request as FlaskRequest

from src.drivers.interfaces.driver_handler_interface import DriveHandlerInterface


class Calculator3:
    def __init__(self, driver_handler: DriveHandlerInterface) -> None:
        self.__drive_handler = driver_handler
    
    def calculate(self, request: FlaskRequest)-> dict: # pyright: ignore[reportInvalidTypeForm]
        body = request.json
        input_data = self.__validate_body(body)
        
        variance = self.__calculate_variance(input_data)
        multiplication = self.__calculate_multiplication(input_data)
        self.__verify_results(variance,multiplication)
        
        response = self.__format_response(variance)
        return response
        
    
    
    def __validate_body(self, body: dict) -> list[float]:
            if "numbers" not in body:
                raise Exception("body mal formatado")
            
            input_data = body["numbers"]
            return input_data
        
    
    def __calculate_variance(self, numbers: list[float]) -> float:
        variance = self.__drive_handler.variance(numbers)
        return variance
    
    
    def __calculate_multiplication(self, numbers: list[float]) -> float:
        multiplication = 1
        for num in numbers: multiplication *= num
        return multiplication
        
    def __verify_results(self, variance: float, multiplication: float) -> None:
        if variance < multiplication:
            raise Exception('falha no processo variencia menor que mutiplicaçao')
    
    def __format_response(self, variance: float) -> dict:
            return {
                "data": {
                    "Calculator":3,
                    "result": float(variance),
                    "success": True
                }
            }