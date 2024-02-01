import pytest 
from lib.present import *

def testing_wrap_function():
    present = Present()
    present.wrap('Present')
    with pytest.raises(Exception) as err:
        present.wrap('Gift')
    error_message = str(err.value)
    assert error_message == "A contents has already been wrapped."

def testing_unwrap_function():
    present = Present()
    with pytest.raises(Exception) as err:
        present.unwrap()
    error_message = str(err.value)
    assert error_message == "No contents have been wrapped."

def test_password_checker_checking_true_value():
    new_password = PasswordChecker()
    true_pass = new_password.check('12345678')
    true_return_value = True
    assert true_pass == true_return_value


def test_password_checker_checking_error_handling():
    new_password = PasswordChecker()
    with pytest.raises(Exception) as e:
        new_password.check('1234')
    error_message = str(e.value)
    assert error_message == 'Invalid password, must be 8+ characters.'
