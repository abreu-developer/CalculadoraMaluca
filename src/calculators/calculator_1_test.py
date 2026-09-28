from src.calculators.calculator_1 import Calculator1
from pytest import ExceptionInfo, raises


class MockRequest:
    def __init__(self, body: dict)-> None:
        self.json = body
    
    
      
def test_calculate():
    mock_request = MockRequest(body={"number": 1})
    
    calculator_1 = Calculator1()
    response = calculator_1.calculate(mock_request)
    
    #format response
    assert "data" in response
    assert "Calculator" in response["data"]
    assert "result" in response["data"]
    
    # assertividade da resposta
    assert response["data"]["result"] == 14.25
    assert response["data"]["Calculator"] == 1
    

def test_calculate_with_body_error():
    mock_request = MockRequest(body={"test": 1})
    calculator_1 = Calculator1()
    
    #error testing
    with raises(Exception) as excinfo: 
        calculator_1.calculate(mock_request)
    
    assert str(excinfo.value) == 'body mal formatado!'