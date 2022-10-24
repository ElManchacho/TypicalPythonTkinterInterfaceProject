from screen import *
from screeninfo import get_monitors

def test_screen():
    screeTest:Screen=Screen()
    assert screeTest.resolution == get_monitors()[0]
