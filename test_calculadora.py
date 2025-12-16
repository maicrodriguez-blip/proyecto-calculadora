import pytest
from calculadora import Calculadora
@pytest.fixture
def calc():
  return Calculadora()
def test_suma(calc):
  assert calc.suma(2, 3) == 5
def test_resta(calc):
  assert calc.resta(5, 2) == 3
def test_divide_normal(calc):
  assert calc.divide(10, 2) == 5
def test_divide_por_cero(calc):
  with pytest.raises(ValueError):
    calc.divide(10, 0)
if __name__ == "__main__":
  pytest.main(["-q"])
