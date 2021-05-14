from src.python.bar.bar import greeting


def build_message() -> str:
    return "Imported greeting: " + greeting()


def say_hello():
    print(build_message())


if __name__ == "__main__":
    say_hello()
