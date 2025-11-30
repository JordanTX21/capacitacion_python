from app.example import Example

def test_increment():
    e = Example("test", 5)
    e.increment(5)
    assert e.value == 10
