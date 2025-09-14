# 리스트에 데이터 추가
# 맨 마지막에 추가하는 방법이 있고, 중간에 추가하는 방법이 있다.

# 리스트 변수
scores = [10, 20, 30]

# append 마지막 추가
scores.append(100)
print(scores) # [10, 20, 30, 100]

a = [10, 20]
b = a
b[0] = 100

print (b) # -> [100, 20]
print (a) #b[0]을 바꾸면 a[0]도 바뀜

# 추가는 index 위치에 추가한다. ex) scores.insert(1, 200) -> 1번 인덱스 위치에 200 추가
scores.insert(1, 200)
print(scores)

# delete 
del scores[0]
print(scores)
scores.pop() # 맨 마지막 요소를 꺼내서 삭제, 그런데 pop() 괄호 안에 숫자를 넣으면 그 값이 삭제됨
print(scores)
