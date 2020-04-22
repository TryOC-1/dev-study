"""데코레이터 예제
  > 클래스 데코레이터
"""


class Modifier:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print(f"before func: {self.func.__name__}")
        result = self.func(*args, **kwargs)
        print(f"after func: {self.func.__name__}")
        return result


@Modifier
def say_hello_deco(name):
    print(f"    hello {name}")


say_hello_deco("jayone")
