# SET의 기본 사용법
# - 중복을 허용하지 않는다.
# - 순서가 없다. (인텍싱으로 접근 불가)
# - 집합연산 가능 (교집합, 합집합, 차집합)
# - 서로 다른 자료형끼리 전환이 가능하다 (리스트 <--> 튜플)

# 1. SET 생성과 중복 제거 예제
print("1. SET의 중복 제거 특성")
numbers_set = {1, 2, 2, 3, 3, 3, 4, 4, 5}  # 중복된 숫자는 자동으로 제거됨
print(f"중복이 제거된 SET: {numbers_set}")  # 출력: {1, 2, 3, 4, 5}

# set
# 중복허용 안함
set_1 = {1,2,3,5,6,4,7,9,8,6}
print('set_1 =', set_1)


# 2. 순서가 없음을 보여주는 예제
print("\n2. SET의 순서 없음 특성")
color_set = {'red', 'blue', 'green'}
print("color_set:", color_set)  # 실행할 때마다 순서가 다를 수 있음
# print(color_set[0])  # TypeError: 'set' object is not subscriptable

# 3. 집합 연산 예제
print("\n3. SET의 집합 연산")
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
print(f"A = {A}")
print(f"B = {B}")

# 교집합 (intersection)
print(f"교집합 (A & B): {A & B}")  # 또는 A.intersection(B) 또는 B.intersection(A)

# 합집합 (union)
print(f"합집합 (A | B): {A | B}")  # 또는 A.union(B) 또는 B.union(A)

# 차집합 (difference)
print(f"차집합 (A - B): {A - B}")  # 또는 A.difference(B) 또는 B.difference(A)

# 4. 자료형 변환 예제
print("\n4. 자료형 변환")
# 리스트 -> SET (중복 제거 활용)
my_list = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
list_to_set = set(my_list)
print(f"리스트에서 SET로 변환 (중복 제거): {list_to_set}")

# 튜플 -> SET
my_tuple = (1, 2, 2, 3, 3, 3)
tuple_to_set = set(my_tuple)
print(f"튜플에서 SET로 변환 (중복 제거): {tuple_to_set}")

# SET -> 리스트 (정렬 등 인덱스가 필요한 작업을 위해)
set_to_list = list(list_to_set)
print(f"SET에서 리스트로 변환: {set_to_list}")

# 5. SET의 주요 메소드 활용
print("\n5. SET 메소드 활용")
fruits = {'apple', 'banana', 'orange'}
print(f"초기 SET: {fruits}")

# 요소 추가
fruits.add('grape')
print(f"'grape' 추가 후: {fruits}")

# 요소 제거 (remove는 요소가 없으면 에러 발생)
fruits.remove('apple')
print(f"'apple' 제거 후: {fruits}")

# 요소 제거 (discard는 요소가 없어도 에러 발생하지 않음)
fruits.discard('melon')  # 없는 요소를 제거 시도해도 에러 없음
print(f"존재하지 않는 'melon' 제거 시도 후: {fruits}")

# SET 비우기
fruits.clear()
print(f"clear() 후 빈 SET: {fruits}")