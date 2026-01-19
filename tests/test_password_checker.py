import pytest
from lib.password_checker import *

def test_password_checker_valid_password():
    password_checker = PasswordChecker()
    result = password_checker.check("password")
    assert result == True

def test_password_checker_invalid_password():
    password_checker = PasswordChecker()
    with pytest.raises(Exception) as e:
        password_checker.check("pswd")
    error_message = str(e.value)
    assert error_message == "Invalid password, must be 8+ characters."