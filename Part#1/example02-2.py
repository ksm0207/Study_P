# 슬라이싱 으로 문자열 나누기

data = "20010331Rainy"
day = data[:8]  # data[:8]은 data[8] 이 포함되지 않습니다
weather = data[8:]  # data[8:] 은 data[8] 을 포함합니다
print("20010331 = ", day)
print("Rainy =  ", weather)

print("Year : ", data[0:4])
print("Day : ", data[4:8])
print("Weather : ", data[8:])

# 슬라이싱 연습문제 나눠서 출력하기
name = "Kimsungmin"
print("First Name = ", name[:3])
print("last Name = ", name[3:])

# Pithon 이라는 문자열을 Python 으로 바꾸기
a = "Pithon"
print(a[:1] + "y" + a[2:])
b = "Namsungmin"
print(b[:0] + "Kim" + b[3:])

# format 함수를 사용한 포매팅
print("I eat {0} apples".format(3))
print("I eat {0} apples".format("One"))
print("I ate {0} apples so I was sick for {1} days !!".format("One", "two"))
print("I ate {0} apples so I was sick for {day} days !!".format("One", day=3))

# f 문자열 포매팅
# 파이썬 3.6 버전부터는 f 문자열 포매팅 기능을 사용 할 수 있습니다
name = "홍길동"
age = 26
print(f"내 이름은 {name} 입니다 나이는 {age} 이예요")
print(f"나는 내년이면 {age+1} 살이 됩니다.")
# f 문자열 포매팅은 name & age 와 같은 변수 값을 참조 할수 있다

# 딕셔너리 활용하기 . key 와 value 라는 것을 한 쌍으로 갖는 자료형 입니다
my = {"name": "홍길동", "age": 30}
print(f"내 이름은 {my['name']} 이고 나이는 {my['age']} 입니다")

# 문자열 관련 함수들

a = "".join("abcd")  # 문자열 삽입
print("Join() = ", a)

b = "lalalalalalalala".upper()  # 소문자 --> 대문자 로 변환
print(b)
c = "LALALALALALALALA".lower()  # 대문자 --> 소문자 로 변환
print(c)

a_strip = "    Hi    ".strip()  # 양쪽 공백 제거
print("strip()=", a_strip)

a_split = "Python Django Flask Wow!!".split()  # 문자열 나누기
print("split()=", a_split)

