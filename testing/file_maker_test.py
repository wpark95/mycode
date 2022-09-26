# import our code called isspace.py
import file_maker
# import our pytest suite
import pytest
# import os module
import os

# our tests are now in a dedicated file
def test_file_maker():
    file_maker.main()

    assert not os.path.exists("the_non_existent.txt")
    assert os.path.exists("test.txt")
