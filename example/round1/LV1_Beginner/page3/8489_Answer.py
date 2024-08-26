import sys

def find_Recycling_bins(location:list, people_num:list) -> int:
    weight_distance = []
    for i in range(len(location)):
        weight_sum = 0
        for j in range(len(location)):
            weight_sum += abs(location[i] - location[j]) * people_num[j]
        weight_distance.append((weight_sum, i+1))

    weight_distance.sort()
    return weight_distance[0][1]
    
    
if __name__=="__main__":
    read = sys.stdin.readline
    write = sys.stdout.write

    N = int(read()) # 아파트 단지의 수

    D = [] # 단지의 위치 리스트
    A = [] # 단지에 거주하는 사람의 수
    for i in range(N):
        location, num = map(int, read().split())
        D.append(location)
        A.append(num)

    ans = find_Recycling_bins(D, A)
    write(str(ans))


'''
[ 중첩 리스트 혹은 리스트의 원소가 튜플일 때의 정렬 ]

sort() 메소드나 sorted() 함수를 사용하면 각 원소(튜플이나 리스트)는 
기본적으로 첫 번째 원소를 기준으로 오름차순 정렬됩니다. 
이는 파이썬이 튜플이나 리스트의 첫 번째 원소를 비교하여 정렬 순서를 결정하기 때문입니다.

만약 첫 번째 원소가 동일한 경우, 파이썬은 두 번째 원소를 비교하여 정렬을 결정합니다. 
이러한 비교는 필요한 만큼 원소의 개수에 따라 계속될 수 있습니다. 

즉, 첫 번째 원소로 정렬 후, 첫 번째 원소가 같을 경우 두 번째 원소로 정렬하는 식으로 
진행됩니다.

---

sort()와 sorted() 둘 다 reverse 옵션이 있다.

    sort()는 리스트의 메소드입니다. 즉, 리스트 객체에 직접 적용되며, 
    해당 리스트를 "제자리에서(in-place)" 정렬합니다. 
    이는 원본 리스트 자체가 변경되며, 정렬된 리스트를 새로운 값으로 반환하지 않습니다
    (None을 반환).   
    사용 예: my_list.sort()

    sorted()는 내장 함수입니다. 
    이 함수는 어떤 이터러블(리스트, 딕셔너리, 튜플 등)에도 사용할 수 있으며, 
    정렬된 새 리스트를 반환합니다. 원본 데이터는 변경되지 않습니다.
    사용 예: new_list = sorted(my_iterable)


    어떤 상황에서 무엇을 사용하는 것이 유리한가?

    원본 데이터를 유지한 채 정렬된 버전이 필요할 때는 sorted()를 사용하는 것이 유리합니다. 
    sorted()는 원본을 변경하지 않고, 새로운 정렬된 리스트를 반환하기 때문에, 
    원본 데이터와 정렬된 데이터를 모두 사용하고 싶을 때 적합합니다.
    
    원본 리스트를 직접 수정해야 하고, 
    새로운 리스트 객체를 생성하는 것을 피하고 싶을 때는 sort()를 사용하는 것이 유리합니다. 
    sort()는 추가 메모리를 할당하지 않기 때문에, 큰 데이터를 다룰 때 메모리 사용량을 줄일 수 있습니다.
    sort()는 리스트에서만 사용할 수 있지만, sorted()는 모든 이터러블에 사용할 수 있다는 점에서 더 범용적입니다.

    
    결론
    메모리 사용량을 최소화하고, 원본 리스트를 바로 변경하고자 할 때 sort()를 사용합니다.
    원본 데이터를 변경하지 않으면서, 다양한 이터러블에 대해 새로운 정렬된 리스트를 얻고자 할 때 sorted()를 사용합니다.

'''