from calculator import add, subtract, multiply, divide

def test_add():
    assert add(2, 3) == 5
    assert add(5, -2) == 3

def test_subtract():
    assert subtract(5, 2) == 3
    assert subtract(10, -3) == 13

def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(5, -2) == -10

def test_divide():
    assert divide(6, 3) == 2
    assert divide(10, 2) == 5
    assert divide(5, 0) == "Cannot divide by zero"

if __name__ == "__main__":
    test_add()
    test_subtract()
    test_multiply()
    test_divide()
    print("All tests passed!")
