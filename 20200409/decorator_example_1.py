"""데코레이터 예제
  > 데코레이터 일반적인 패턴
"""
def modifier(func):
    def wrapper():
        print(f'before func: {func.__name__}')
        result = func()
        print(f'after func: {func.__name__}')
        return result
    
    return wrapper


# 적용 
def hello_world():
    print('    hello world')


hello_world = modifier(hello_world)
hello_world()


# 데코레이터를 사용한 적용
@modifier
def hello_world_deco():
    print('    hello world')


hello_world_deco()
