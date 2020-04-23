# 적용할 함수
import time


class Modifier:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        ts = time.time()
        result = self.func(*args, **kwargs)
        te = time.time()
        print("Function", self.func.__name__, "time:", round((te - ts) * 1000, 1), "ms")
        return result


@Modifier
def func(times: int) -> str:
    count = 0
    for _ in range(times):
        count += 1
    return f"{count}번 계산 완료했습니다."


@Modifier
def say_hello_deco(name):
    for _ in range(5):
        print(f"    hello {name}")


if __name__ == "__main__":
    result = func(10000000)
    print(result)
    say_hello_deco("jayone")
