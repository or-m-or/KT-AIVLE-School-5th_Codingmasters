
# No 3. 순열, 조합


```python
print('-----------[ 순열 조합 생성 ]------------')
from itertools import permutations

lista = [3, 2, 5, 4, 1]
nPr = permutations(lista, 3) # literable 객체, nPr의 r 값 / return itertools 객체
print('1) 순열 리스트 반환 (input:[3,2,5,4,1]) :\n',list(nPr))


from itertools import combinations

nCr = combinations(lista, 3) # literable 객체, nCr의 r 값 / return itertools 객체
print('2) 조합 리스트 반환 (input:[3,2,5,4,1]) :\n',list(nCr))
```
