# Q8503 : 기둥 세우기

> 요약 : 

오래된 궁전이 세월의 무게를 이기지 못하고 무너지려고 합니다. <br>
관리당국에서는 궁전 곳곳에 기둥을 세우는 보수 공사를 하려고 합니다. <br>
<br>
직사각형 형태의 궁전을 형성하는 모든 가로, 세로 줄에 대해서 <br>
적어도 기둥이 하나씩은 존재하도록 만들고자 할 때,<br>
세워야 하는 기둥의 최솟값을 출력하는 프로그램을 작성하세요.<br>
<br><br>

## 입력값 설명
첫째 줄에 궁전의 세로 크기 N과 가로 크기 M이 주어집니다.<br>
N과 M은 50보다 작거나 같은 자연수입니다.<br>
<br>
둘째 줄부터 N개의 줄에는 궁전의 상태가 주어집니다.<br>
궁전의 상태는 1은 빈칸, 0은 기둥이 있는 칸입니다.<br>


## 출력값 설명
세워야 하는 기둥의 최솟값을 출력합니다.<br>
<br><br>

> **예제 입력1**
```
3 3
1 1 1
1 1 1
1 1 1
```

> **예제 출력1**
```
3
```
<br>

> **예제 입력2**
```
4 3
0 1 1
1 0 0
0 1 0
1 0 1
```

> **예제 출력2**
```
0
```