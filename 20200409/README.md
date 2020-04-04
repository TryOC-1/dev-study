# 데코레이터 이해하기



## 기본 개념

- 데코레이터는 함수와 메서드의 기능을 쉽게 수정하기 위한 수단으로 제공된 기능
- 기능 자체는 단순하게 데코레이터 이후에 나오는 것을 첫 번째 파라미터로 하고 데코레이터의 결과 값을 반환하게 하는 것으로 단순함
  - decorator_example_1.py 참조
- 원래는 함수와 메서드를 위해 고안 되었지만 실제로는 어떤 종류의 객체에도 적용이 가능하기 때문에 함수와 메서드, 제너레이터, 클래스에 데코레이터 적용 가능



## 과제

1. 데코레이터 개념 이해하기
   - 해당 문서 참조 : [python decorator (데코레이터) 어렵지 않아요](https://bluese05.tistory.com/30)
2. 함수 실행시간 측정하는 데코레이터 작성하기 (`클래스`, `함수` 데코레이터 모두)
   - 해당 링크 참조 : https://stackoverflow.com/questions/4887081/get-the-name-of-a-decorated-function#42086220
   - decorator_example_2.py, decorator_example_3.py 참조
   - 적용할 함수는 func_example.py 참조
3. `@wraps` 의 기능에 대해 이해하기
   - 해당 링크 참조 (2와 같은 링크) : https://stackoverflow.com/questions/4887081/get-the-name-of-a-decorated-function#42086220
4. 실제로 데코레이터가 쓰이는 곳 살펴보기
   - Airflow 소스 내에서(최신 버전 기준) : https://github.com/apache/airflow