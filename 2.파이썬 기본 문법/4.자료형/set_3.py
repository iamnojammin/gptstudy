# tuple, list, set
# tuple : 순서가 있고, 중복을 허용한다. 수정이 불가능하다(immutable)
tuple_1 = (1,2,3,4,5,1,2,3,)
tuple_2 = (10, 20)
print('tuple_1 + tuple_2 =', tuple_1 + tuple_2)
print('tuple_1 * 3 =', tuple_1 * 3) #튜플 반복
print('tuple_1[0] =', tuple_1[0]) #튜플 인덱싱
print('tuple_1[1:4] =', tuple_1[1:4]) #튜플 슬라이싱, 끝번호-1까지

print('len(tuple_1) =', len(tuple_1)) #튜플 길이
print('len(tuple_1) =', len(tuple_1)-1) #튜플 마지막 인덱스
print('len(tuple_1) =', tuple_1[-1]) #튜플 마지막 값

print('tuple_1.count(1) =', tuple_1.count(1)) #튜플에서 특정 값의 개수 세기

# 튜플의 데이터중에서 만지막 3개를 출력
print('tuple_1[-3:] =', tuple_1[-3:])   #튜플 슬라이싱, 끝번호-1까지
# 튜플의 데이터중에서 처음 3개를 출력
print('tuple_1[:3] =', tuple_1[:3])   #튜플 슬라이싱, 끝번호-1까지
# 역방향 출력은
print('tuple_1[::-1] =', tuple_1[::-1])   #튜플 슬라이싱, 끝번호-1까지

