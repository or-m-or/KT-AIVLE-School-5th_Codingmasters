# 파이썬 코딩테스트에서 자주 사용되는 내장 함수

#### `all(iterable)`
> 이터러블의 모든 요소가 True인지 확인합니다.
```python
print(all([1, True, 'a']))  # Output: True
print(all([1, False, 'a']))  # Output: False


>>> True
>>> False
```


#### `any(iterable)`
> 이터러블의 요소가 True인지 확인합니다.
```python
print(any([0, False, '']))  # Output: False
print(any([0, True, '']))  # Output: True


>>> False
>>> True
```


#### `chr(i)`
> 아스키코드 값(int)을 입력 받고, 대응되는 문자를 반환합니다. 
```python
# 아스키코드 값 65에 대응되는 문자를 반환합니다.
print(chr(65))
>>> 'A'

# 아스키코드 값 97에 대응되는 문자를 반환합니다.
print(chr(97))
>>> 'a'
```


#### `ord(c)`
> 유니코드 문자(char)을 입력 받고, 대응되는 아스키코드 값을 반환합니다.
```python
# 문자 'A'에 대응되는 아스키코드 값을 반환합니다.
print(ord('A'))
>>> 65

# 문자 'a'에 대응되는 아스키코드 값을 반환합니다.
print(ord('a'))
>>> 97
```


#### `divmod(a, b)`
> a를 b로 나눈 몫과 나머지를 반환합니다.
```python
print(divmod(9, 4))  # Output: (2, 1)


>>> (2, 1)
```


#### `enumerate(iterable, start=0)`
> 열거형 객체를 반환합니다.
```python
for i, v in enumerate(['a', 'b', 'c'], start=1):
    print(f'{i}: {v}')


>>> 1: a
>>> 2: b
>>> 3: c
```


#### `eval()`
> 수학 수식이 문자열 형식으로 들어오면 해당 수식을 계산한 결과를 반환
```python
result = eval("(3 + 5) * 7")
print(result)


>>> 56
```



#### `filter(function, iterable)`
> 이터러블에서 요소를 필터링합니다.
```python
for i, v in enumerate(['a', 'b', 'c'], start=1):
    print(f'{i}: {v}')


>>> [1, 2]
```


#### `isinstance(object, classinfo)`
> 객체가 클래스의 인스턴스인지 확인합니다.
```python
print(isinstance(5, int))  # Output: True


>>> True
```


#### `len(s)`
> 객체의 길이를 반환합니다.
```python
print(len('hello'))  # Output: 5


>>> 5
```


#### `map(function, iterable)`
> 이터러블의 모든 항목에 함수를 적용합니다.

```python
result = map(lambda x: x * 2, [1, 2, 3])
print(list(result))  # Output: [2, 4, 6]


>>> [2, 4, 6]
```


#### `max(iterable, *[, key, default])`
> 파라미터가 2개 이상 들어왔을 때 가장 큰 값 반환
```python
result = max(7, 3, 5, 2)
print(result)


>>> 7
```


#### `min(iterable, *[, key, default])`
> 파라미터가 2개 이상 들어왔을 때 가장 작은 값 반환
```python
result = min(7, 3, 5, 2)
print(result)


>>> 2
```

#### `range(start, stop[, step])`
> 일련의 숫자를 생성합니다.
```python
for i in range(3):
    print(i)  # Output: 0 1 2


>>> 0
>>> 1
>>> 2
```


#### `reversed(seq)`
> 역방향 이터레이터를 반환합니다
```python
for i in reversed([1, 2, 3]):
    print(i)  # Output: 3 2 1


>>> 3
>>> 2
>>> 1
```


#### `sorted(iterable, *, key=None, reverse=False)`
> iterable 객체가 들어왔을 때, 정렬된 결과를 반환 <br>
- key 속성으로 정렬 기준을 명시할 수 있음
- reverse 속성으로 정렬된 결과 리스트를 뒤집을 지의 여부 설정할 수 있음
- 리스트와 같은 iterable 객체는 기본으로 sort() 함수를 내장하고 있어서 <br> 
  sort() 함수로도 정렬 가능, 이 경우에는 리스트 객체의 내부 값이 정렬된 값으로 바로 변경됨

```python
result = sorted([9, 1, 8, 5, 4])
print(result)

>>> [1, 4, 5, 8, 9]

result = sorted([9, 1, 8, 5, 4], reverser = True)
print(result)

>>> [9, 8, 5, 4, 1]

result = sorted([('홍길동', 35), ('이순신', 75), ('아무개', 50)], key = lambda x: x[1], reverse = True)
print(result)

>>> [('이순신', 75), ('아무개', 50), ('홍길동', 35)]

data = [9, 1, 8, 5, 4]
data.sort()
print(data)

>>> [1, 4, 5, 8, 9]
```


#### `sum(iterable, /, start=0)`
>  iterable 객체(리스트, 사전 자료형, 튜플 자료형 등)의 모든 원소의 합 반환
```python
result = sum([1, 2, 3, 4, 5])
print(result)


>>> 15
```


#### `zip(*iterables)`
> 튜플의 이터레이터를 반환하며, 여기서 i번째 튜플은 각 인자 시퀀스 또는 이터러블에서 i번째 요소를 포함합니다.


```python
for item in zip([1, 2], ['a', 'b']):
    print(item)  # Output: (1, 'a') (2, 'b')


>>> (1, 'a')
>>> (2, 'b')
```


#### `oct(x:int) -> str`
> int를 입력받고, 접두사 '0o'가 붙은 8진수를 문자열로 반환합니다.

```python
oct(8)
>>> '0o10'

oct(-56)
>>> '-0o70'
```


#### `hex(x:int) -> str`
> int를 입력받고, 접두사 '0x'가 붙은 16진수를 문자열로 반환합니다.

```python
hex(255)
>>> '0xff'

hex(-42)
>>> '-0x2a'
```
