from src.calculators.calculator_2 import Calculator_2
from src.drivers.interfaces.driver_handler_interface import DriveHandlerInterface
from src.drivers.numpy_handler import NumpyHandler


class MockRequest:
    def __init__(self, body: dict)-> None:
        self.json = body


class MockDriverHandler(DriveHandlerInterface):
    
    def standard_derivation(self, numbers: list[float]) -> float:
        return 3
    
    def variance(self, numbers: list[float]) -> float:
        pass
    
    
# integraçao entre nump e a calc_2
def test_calculate_integration():
    mock_request = MockRequest(body={"numbers": [1,2,3,4,5]})
    
    driver = NumpyHandler()
    calculator_2 = Calculator_2(driver)
    format_response = calculator_2.calculate(mock_request)
 
    assert isinstance(format_response, dict)
    assert format_response == {'data': {'Calculator': 2, 'result': 0.08}}
    
    
def test_calculate():
    mock_request = MockRequest(body={"numbers": [1,2,3,4,5]})
    
    driver = MockDriverHandler()
    calculator_2 = Calculator_2(driver)
    format_response = calculator_2.calculate(mock_request)
 
    assert isinstance(format_response, dict)
    assert format_response == {'data': {'Calculator': 2, 'result': 0.33}}