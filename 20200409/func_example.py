# 적용할 함수
def func(times: int) -> str:
    count = 0
    for _ in range(times):
        count += 1

    return f'{count}번 계산 완료했습니다.'


if __name__ == '__main__':
    result = func(10000000)
    print(result)
