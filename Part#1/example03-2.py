# 리스트 관련 함수들

# 1. 리스트에 요소 추가 하기 .append

value = 500
a = [1, 2, 3]
a.append(value)
print("예상결과 : 1 2 3 500", a)

s_value = "Apple"
b = ["Bababa", "Water Melon", "Tomato"]
b.append(s_value)
print(b)

# 리스트 정렬
sort_index = [1, 5, 2, 3, 49, 221, 99]
result = sort_index
result.sort()
print(result)

# 리스트 요소 삽입
insert_index = [10, 20, 30, 40]
insert_index.insert(0, 0)  # 0번째 자리에 0을 더하라는것
print(insert_index)

# 리스트 요소 제거
remove_index = [1, 2, 3, 4, 5, 6, 7]
remove_index.remove(7)
print("remove = ", remove_index)

# 리스트 요소 끄집어 내기
pop_index = [50, 100, 150, 200]
pop_index.pop(0)  # 값을 끄집어내면 해당 값은 삭제 된다
print("Pop = ", pop_index)

# 리스트 확장

extend_index = [1, 2, 3]
extend_index.extend([4, 5])
print("예상결과 1 2 3 4 5 ", extend_index)
b_extend_index = [6, 7]
extend_index.extend(b_extend_index)
print("예상결과 : 1 2 3 4 5 6 7", extend_index)
