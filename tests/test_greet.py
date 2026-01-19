from lib.greet import *

def test_greet_with_david():
    result = greet("David")
    assert result == "Hello, David!"