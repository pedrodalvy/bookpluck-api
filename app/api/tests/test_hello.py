from app.api import hello


def test_should_return_hello_message_when_call_home() -> None:
    greetings = hello.home()

    assert greetings == "Hello, Flask!"
