# Python Built-in Functions Examples

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
> 이터러블에서 가장 큰 항목을 반환합니다.
```python
print(max([1, 2, 3]))  # Output: 3


>>> 3
```


#### `min(iterable, *[, key, default])`
> 이터러블에서 가장 작은 항목을 반환합니다.
```python
print(min([1, 2, 3]))  # Output: 1


>>> 1
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
> 이터러블의 항목에서 정렬된 목록을 반환합니다.
```python
print(sorted([3, 1, 2]))  # Output: [1, 2, 3]


>>> [1, 2, 3]
```


#### `sum(iterable, /, start=0)`
> 합계가 시작되고 이터러블의 항목이 왼쪽에서 오른쪽으로 이동합니다.
```python
print(sum([1, 2, 3]))  # Output: 6


>>> 6
```


#### `zip(*iterables)`
> 튜플의 이터레이터를 반환하며, 여기서 i번째 튜플은 각 인자 시퀀스 또는 이터러블에서 i번째 요소를 포함합니다.


```python
for item in zip([1, 2], ['a', 'b']):
    print(item)  # Output: (1, 'a') (2, 'b')


>>> (1, 'a')
>>> (2, 'b')
```