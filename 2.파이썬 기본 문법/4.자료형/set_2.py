# 리스트 연산자
list_1 = [1, 2, 3]
list_2 = [4, 5, 6]
print('list_1 + list 2 =', list_1 + list_2) # 리스트 연결, 즉 리스트끼리는 + 연산만 가능
print('list_1 * 3 =', list_1 * 3) # 리스트 반복, 즉 리스트에는 상수만 곱할 수 있음

list_1.append(list_2)
print(list_1)
print(list_1[3][1])

# set
# 중복허용 안함
set_1 = {1,2,3,5,6,4,7,9,8,6}
print('set_1 =', set_1)
# print(set_1[0]) # set은 순서가 없기 때문에 인덱싱 불가
# set에서 특정 위치에 단일 값에 접근하려면
# print('set_1에서 단일 값에 접근 = ', list(set_1[0]))
# set은 집합 연산이 가능하다
set_1 = {1,2,3,4,5}
set_2 = {4,5,6,7,8}
# 교집합
print('set_1 & set_2 =', set_1 & set_2)
print('set_1.intersection(set_2) =', set_1.intersection(set_2))
# 합집합
print('set_1 | set_2 =', set_1 | set_2)
print('set_1.union(set_2) =', set_1.union(set_2))
# 차집합
print('set_1 - set_2 =', set_1 - set_2) # set_1에는 있지만 set_2에는 없는 값
print('set_1.difference(set_2) =', set_1.difference(set_2))
# set_2에는 있지만 set_1에는 없는 값