from hellodoodle import say_hello

def test_hellodoodle_no_params():
    assert say_hello() == "Hello, world!"

def test_hellodoodle_with_params():
    assert say_hello("Everybody") == "Hello, Everybody!"