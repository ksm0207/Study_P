# 문자열 자료형

# 문자열 만드는 방법

a = "큰따옴표로 양쪽 둘러싸기"
b = "작은 따옴표로 양쪽 둘러싸기"
c = """ 큰따옴표 3개를 연속으로 써서 둘러싸기 """
d = """ 작은따옴표 3개를 연속으로 둘러싸기"""

print(a, b, c, d)

# 문자열 안에 작은따옴표나 큰 따옴표를 포함시키고 싶을때
food = "My name is 'Kim'"
print(food)

# Error : SyntaxError .. Python 이 문자열로 인식되어 구문 오류 발생합니다
# food = 'Python's favorite food is perl'


# 문자열에 큰 따옴표 포함시키기
say = '" 먼저 문자열을 작은따옴표로 둘러싸기" 작동되나요?'
print(say)

# 여러 줄인 문자열을 변수에 대입하고 싶을때 이스케이프 코드 \n 삽입하기
say = "Life is too short \n You need Python "
print(say)

# 문자열 연산하기

day = "Mon"
day2 = "Tue"
result = day + day2
print(result)

# 문자열 곱하기
print("=" * 50)
print("Hello")
print("=" * 50)

# 문자열 길이 구하기 내장함수 len() 사용하기
lang = "lalalalalalalalalala"
print("This is  = ", len(lang))

# 문자열 인덱싱과 슬리이싱
# 인덱싱 : 무언가를 가르킨다는 의미
# 슬라이싱 : 무엇인가를 잘라낸다 는 의미
lang = "Life is Too short, You need Python"
#      0123 4 56789012345678901234567890123
#      L은 첫번째 자리 숫자를 뜻하는 숫자 0을 의미 바로 다음인 i는 1 이런식으로 계속 번호가 붙여진다
print("'L' i f e = ", lang[0])
print("L 'i' f e = ", lang[1])  # lang[번호]는 문자열 안의 특정한 값을 뽑아내는것인데 이것을 인덱싱 이라고 합니다
print("L i 'f' e = ", lang[2])
print("L i f 'e' = ", lang[3])

print("L i f 'e' = ", lang[-2])

# 문자열 슬라이싱 Life 만 뽑아보기
print("Result = ", lang[0] + lang[1] + lang[2] + lang[3])

# 0:4 는 시작되는 문장에서 자리 번호 0부터 4까지 문자를 가져온다는 뜻입니다
print("슬라이싱 기법 : ", lang[0:4])
# 슬라이싱 기법으로 lang[시작:끝번호] 를 지정할때 끝 번호에 해당하는것은 포함하지 않습니다
print("슬라이싱 기법 : ", lang[0:3])
print("슬라이싱 기법 : ", lang[0:2])
print("슬라이싱 기법 : ", lang[0:1])

# 문자열 슬라이싱 - 공백문자도 문자열로 포함됩니다
print("슬라이싱 기법 : ", lang[0:5])

print("is : ", lang[5:7])
print("short : ", lang[12:17])  # lang[시작번호:끝번호(포함x)]

