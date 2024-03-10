# NO 1. 데이터 입력

#### Standard - `input()`

    - 프롬프트 입력 -> \n 제거 -> 문자열로 변경 -> return
    - 더 이상 입력 X -> EOFError

#### Skill - `sys.stdin`

    - 프롬프트 입력 -> Buffer에 저장 -> 요청이 오면 읽음.
    - sys.stdin 은 객체(File Object)이다.
    - .readline() 은 EOF에 도달하면 빈 문자열 반환
    - .readline() 은 '\n'까지 읽어옴 -> .strip()으로 제거 필요


## 📌 1. 정수 N개, 한 줄 입력

```python
import sys

read = sys.stdin.readline
N, M, K = map(int, read().split())
```


## 📌 2. 정수 N개, 한 줄 입력 -> List 저장

```python
import sys

read = sys.stdin.readline
data = list(map(int, read().split()))
```


## 📌 3. 정수 N개, 여러 줄로 입력 -> List 저장

```python
import sys

read = sys.stdin.readline
N = int(read())
data = [int(read()) for _ in range(N)]

# 방법1. List 생성 -> append()
# 밥법2. List Comprehension
```

## 📌 4. 문자열 N개, 여러 줄 입력, -> List 저장

```python
import sys

read = sys.stdin.readline
N = int(read())
data = [read().strip() for _ in range(N)] 

# strip() 함수를 통해 문자열에 붙은 개행문자 제거
```


## 📌 5. 정수 N개, 여러 줄 입력, -> 2차원 배열 저장

```python
import sys

read = sys.stdin.readline
N = int(read())
matrix = [list(map(int, read().split())) for _ in range(N)]
```