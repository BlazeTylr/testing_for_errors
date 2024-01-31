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