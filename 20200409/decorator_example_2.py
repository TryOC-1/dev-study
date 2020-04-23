"""데코레이터 예제
  > 함수 인자값 전달하기
"""


def modifier(func):
    def wrapper(*args, **kwargs):
        print(f"before func: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"after func: {func.__name__}")
        return result

    return wrapper


@modifier
def say_hello_deco(name):
    print(f"    hello {name}")


say_hello_deco("jayone")
