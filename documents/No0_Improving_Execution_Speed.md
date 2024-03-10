# Python 코딩테스트 실행 속도 개선 방법

1. 내장 함수 활용
2. Generator로 메모리 아끼기
3. for / while보다 빠른 반복
4. dictionary와 set으로 조회
5. 내장 모듈의 자료구조
6. 빠르게 문자열 합치기
7. 빠른 입출력
8. global 참조 피하기
9. dot 줄이기
10. 불필요한 연산, 호출 줄이기


## 1. 내장 함수 활용

- Python이 기본 제공하는 내장 함수는 C로 작성됨. <br>
- Built-in-Functions: https://docs.python.org/ko/3/library/functions.html
- 유용한 함수: all, any, divmod, enumerate, filter, isinstance, len, map, max, min, range, reversed, sorted, sum, zip

## 2. Generator로 메모리 아끼기
- generator를 사용한다 것 = 도구가 필요할 때만, 꺼내 쓰는 것
- 공간 절약 가능, 익히 아는 range( )도 generator를 생성함.

1. yield 사용
2. Comprehension 활용

```python
# Generator Comprehension
even = (n*2 for n in range(100))
 
# 사용법
for i in even:
    print(i)
```


## 3. for / while 보다 빠른 반복
1. Comprehension 활용하기
    - 생각보다 많은 사람들이 Generator Comprehension에 대해 잘 모르고 있다.
    - 단순히 ```[ ]```로 감싸면 ```list```, ```( )```로 감싸면 ```generator```를 반환한다.
    - 만약 단순 반복이 목적이라면 ```( )```를 활용할 수 있다.
    - 하지만 list 객체의 메서드를 활용하거나 직접 list를 조작해야 한다면 ```[ ]```를 사용하면 된다.

2. map, filter
    - map과 filter는 위에서도 소개했던 Python 내장 함수 중 하나
    - ```map```    : 함수를 입력받아 모든 값에 대하여 함수를 적용해준다.
    - ```filter``` : 모든 값 중 조건(true를 반환하는 함수)에 해당하는 값만을 반환한다. 

```python
# 1. Comprehension

[i*2 for i in range(100)] # -> list
(i*2 for i in range(100)) # -> generator
```

```python
# 2. map, filter

# map
a = map(int, ["3", "7", "9"])
a = list(a)
 
# map을 for문으로 작성하면
a = []
for n in ["3", "7", "9"]:
    a.append(int(n))
 
 
# filter
a = filter(lambda x: x%2==0, [2, 5, 6, 9])
a = list(a)
 
# filter를 for문으로 작성하면
a = []
for n in [2, 5, 6, 9]:
    if n % 2 == 0:
        a.append(n)
```


#### 4. dictionary와 set으로 조회
- 일반적으로 값을 list에 많이 저장하지만 ```list```는 값을 찾기 위해 처음부터 끝까지 하나씩 살펴봄. 따라서 ```O(N)``` 시간이 소요
- 대신 ```dictionary```는 ```O(1)```로 한 번에 값을 조회할 수 있다. 이는 Dictionary가 ```Hash Table```이라는 구조를 사용하기 때문

- ```Dictionary```는 ```key-value``` 형태로 맵핑되어 있는 한 쌍의 데이터를 저장한다. 
- 만약 **단일 데이터의 조회가 목적**이라면 ```set```을 사용할 수 있다. 

- ```set```은 '집합'이라는 개념으로 추상화되어 있지만, 실질적으로 ```key```만 있는 ```dictionary```라고 생각하면 된다. 
- dictionary의 key와 같이 **순서가 없고, 중복이 없다.** 
- 값을 조회하는 시간도 ```O(1)```로 동일하다.


#### 5. 내장 모듈의 자료구조 사용
- Python은 자체적으로 완성도 높은 자료구조를 제공한다.
- 대표적으로 ```deque```, ```Counter```, ```defaultdict``` 등이 있다. 
- 특히 ```deque```는 Python으로 코테를 한다면 몰라서는 안 되는 자료구조이다. 
- 상황에 따라 list에 비해 효율적으로 값을 저장하고 제거할 수 있기에 많이 사용된다. 

참고 : https://docs.python.org/ko/3/library/collections.html


#### 6. 빠르게 문자열 합치기
- ```f-string``` 포맷팅 기능사용
- ```f-string```은 가독성이 좋은 뿐만 아니라 성능도 뛰어나다. 
- 만약 섬세한 포맷팅 없이 문자를 이어 붙이는 것이 목적이라면 ```Join```으로 간단하게 처리할 수 있다. 
- **결과를 줄 바꿈으로 출력**하거나 **한 칸씩 띄워서 한 줄에 출력**하라는 형식의 문제들이 많다. -> ```Join``` 사용 


```python
res = 33
f"RES: {res}"

"\n".join(["1st", "2nd", "3rd"])
" ".join(map(str, [1, 2, 3]))
```


#### 7. 빠른 입출력
```python
import sys
 
sys.stdin.readline() # 입력
sys.stdout.write()   # 출력
```


Python은 함수 자체를 변수에 저장할 수 있기 때문에 아래와 같이 작성할 수 있다. 
```python
import sys
# 정의
input = sys.stdin.readline
print = sys.stdout.write 
# 실행
input().rstrip("\n")
print()
```

- ```readline```은 끝에 **줄 바꿈('\n')까지 읽어온다.** 
- 따라서 **strip을 통해 '\n'을 제거**해야 우리가 아는 input과 동일하게 사용할 수 있다. 
- ```print```는 모든 타입의 데이터를 받지만 ```write```는 문자열만을 출력한다. 
- 따라서 **다른 타입의 데이터가 있다면 문자열로 변경 후 출력**해야 한다. 
- 이때 위에서 봤던 ```f-string```이나 ```join```을 활용하면 아주 효율적으로 출력이 가능해진다. 

```python
import sys
 
print = sys.stdout.write  
 
res = [3, 7, 1, 9]
print(" ".join(map(str, res)))  # 3 7 1 9
print(res) # 오류
```

#### 8. Global 참조 피하기
- ```global```을 통해 전역 변수 참조 -> 성능이 저하될 수 있음. 
- ```global```은 단순히 성능에 영향을 줄 뿐만 아니라, 예상치 못한 오류를 발생시킬 수 있기 때문 -> 일반적인 코드에서도 지양됨. 
- ```global``` 값을 참조해야 하는 상황이라면 -> 함수 파라미터로 값을 전달, 또는 OOP로 설계하는 등 대안을 사용하는 것이 안전 


### 9. dot 줄이기
- ```dot```은 클래스에 접근하거나 패키지에 접근할 때 사용하는 ```.```를 이야기한다. 
- 아주 사소한 부분이지만 성능에 영향을 줄 수 있는 요소이다. 


```python
class Count():
    def __init__(self):
        self._n = 0

    def count1(self, nums: list):
        # dot 여러번 사용
        for i in nums:
            self._n += i

    def count2(self, nums: list):
        # dot 2번만 사용
        n = self._n
        
        for i in nums:
            n += i
        self._n = n
```


이렇게 작성하는 것이 파이썬다운 방식인지에 대해서는 의문이다. 다만 속도 향상에 도움이 된다면 시도해 볼 수 있다. 
```python
# Bad
import math
math.sqrt()
 
# Good
from math import sqrt
sqrt()
```
모듈 전체를 불러와 사용하면 성능에 문제가 될 수 있다. 또한 대부분의 경우, 구체적인 함수를 불러와 사용하는 것이 가독성을 높여준다. 