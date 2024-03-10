# No 1. 데이터 출력

#### Standard - `print()`

    - python 표준 입출력

#### Skill 1 - Packing, Unpacking
    
    - `Packing` : 하나의 변수에 여러 개의 값을 넣는 기법
    - `Unpacking` : tuple 로 묶인 값들을 다시 풀어주는 기법
    - 흔히 tuple 자료형을 사용할 경우 이 기법을 많이 채용함.
    - 이를 잘 활용한다면, List 에 담긴 값을 반복문 없이도 쉽게 출력시킬 수 있다.

> example
```python
numbers = 1, 2, 3, 4
N, M, K, L = numbers
```


#### Skill 2 - Asterisk

    - Asterisk (*) 는 Python 에서 다양한 용도로 사용되는 특수 문자 중 하나다.
    - 곱셉, 리스트 확장의 등의 기능도 있으나, Unpacking 을 진행할 때도 쓰인다.
    -  for 문 없이도 data 변수가 자동으로 언패킹 되어 화면에 출력할 수 있다.

> example
```python
data = [1, 2, 3, 4, 5]
print(*data)


>>> 1 2 3 4 5
```


#### Skill 3 - `sys.stdout.write`

    - `sys.stdout.write`는 표준 출력(stdout)에 직접 문자열을 쓰기 위해 사용되는 메서드

    - `print`는 기본적으로 출력할 데이터 끝에 개행 문자(`\n`)를 추가하지만
    - `sys.stdout.write`는 이를 자동으로 추가하지 않음. 
    - 따라서 개행이 필요할 경우, 명시적으로 `\n`을 문자열에 포함시켜야 함.
    - `sys.stdout.write`는 문자열만을 인자로 받음 
    - 다른 타입의 객체를 출력하려면 문자열로 변환해야 함. 
    - `print` 함수는 여러 타입의 객체를 자동으로 문자열로 변환함.
    - `sys.stdout.write`는 출력된 문자열의 길이를 정수로 반환함.


## 📌 1. 기본 출력

```python
import sys

# 문자열 출력
sys.stdout.write("Hello, World!\n")

# 변수를 포함한 문자열 출력
name = "Python"
sys.stdout.write(f"Hello, {name}!\n")

# 개행을 포함하여 여러 줄 출력
sys.stdout.write("Line 1\nLine 2\n")

# 문자열이 아닌 객체 출력 (객체를 문자열로 변환)
number = 42
sys.stdout.write(str(number) + "\n")


>>> Hello, World!
>>> Hello, Python!
>>> Line 1
>>> Line 2
>>> 42 
>>> 3

```


## 📌 2. 0부터 9까지 숫자를 한 줄에 출력

```python
for i in range(10):
    sys.stdout.write(str(i))
sys.stdout.write("\n")  # 모든 숫자 출력 후 개행


>>> 0123456789
>>> 1
```


## 📌 3. ' '.join 사용

```python
data = '테스트'
sys.stdout.write(' '.join(data) + '\n')


>>> 테 스 트
>>> 6
```