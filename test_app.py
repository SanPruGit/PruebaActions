from app import hello

def test_hello(capsys): 
    hello()
    captured = capsys.readbuterr()
    assert captured.out == "Hola Mundo\n"