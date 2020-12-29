# 리스트 자료형

# 리스트의 인덱싱과 슬라이싱
# #1 인덱싱

a = [1, 2, 3]
print("첫번째 요소값 ", a[0])
print("첫번째 요소값 + 세번째 요소값 = ", a[0] + a[2])

b = [1, 2, 3, ["a", "b", "c"]]
print("b[3] = ", b[3])
print("마지막 요소값 ", b[-1])
print("a값만 빼기 ", b[-1][0])

c = [1, 2, ["a", "b", ["Life", "is"]]]
print("삼중 리스트 에서 Life 값만 빼기", c[2][2][0])

# #2 슬라이싱

index = [1, 2, 3, 4, 5]
print("1 2 ", index[0:2])

b_index = index[:2]
print("1 2 ", b_index)

c_index = index[2:]
print("3 4 5 ", c_index)

# 리스트 연산하기

num = [1, 2, 3, 4, 5]
num2 = [6, 7, 8, 9, 10]
result = num + num2  # 리스트 사이의 + 는 합치는 기능을 합니다
print("리스트 연산 결과 : ", result)

q = [1, 2, 3]
q_result = q * 3
# string = "abc" * 3 이와 같은 이치 이다
print("Q = ", q_result)

index_len = ["apple", "banana", "watermelon", "tomato"]
print("리스트 길이 구하기 : ", len(index_len))
# len 함수는 문자열 리스트 외에 튜플 및 딕셔너리에도 자주 사용 합니다

exm = [1, 2, "3"]
plus = exm[2] + "hi"
print(plus)

# 리스트의 수정과 삭제
i_from = [1, 2, 3]
i_from[2] = 4
print(i_from)

s_from = ["Python", "Java", "JSP", "PHP", "Go"]
s_from[1] = "Django"
print(s_from)

del s_from[1]  # del 키워드는 리스트의 요소를 삭제할수있다
print(s_from)

index_number = [1, 2, 3, 4, 5, 6]
del index_number[:3]
print("예상결과 : 4 5 6 = ", index_number)
