from pytest import raises

from src.calculators.calculator_3 import Calculator3


class MockRequest:
    def __init__(self, body: dict) -> None:
        self.json = body


class MockDriverHandlerERROr:

    def variance(self, numbers: list[float]) -> float:
        return 3


class MockDriverHandler:

    def variance(self, numbers: list[float]) -> float:
        return 10000000


def test_calculate_with_variance_error():
    mock_request = MockRequest({"numbers": [1, 2, 3, 4, 5]})
    calculator3 = Calculator3(MockDriverHandlerERROr())

    with raises(Exception) as exinfo:
        calculator3.calculate(mock_request)

    assert str(exinfo.value) == "falha no processo variencia menor que mutiplicaçao"


def test_calculate():
    mock_request = MockRequest({"numbers": [1, 1, 1, 1, 100]})
    calculator3 = Calculator3(MockDriverHandler())

    response = calculator3.calculate(mock_request)
    print(response)

    assert response == {'data': {'Calculator': 3, 'result': 10000000.0, 'success': True}} 