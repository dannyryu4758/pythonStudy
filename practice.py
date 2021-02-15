# 양수로 만들기
# print(abs(-5)) # 5
# O 제곱 구하기
# print((pow(4,2))) # 4^2 = 4*4 = 16
# 큰값/작은값 구하기
# print(max(5,12)) # 12
# print(min(5,12)) # 5
# 반올림하기
# print(round(3.24)) # 3
# print(round(4.99)) # 5

###########################################################

# # math 라이브러리
# from math import *
# print(floor(4.99)) # 내림 4
# print(ceil(3.14)) # 올림 4
# print(sqrt(16)) # 제곱근 4 (루트)

# 3

# # random 라이브러리
# from random import *
# print(random()) # 0.0 ~ 1.0 미만의 임의의 값 생성 (소수점)
# print(randrange(1,46)) # 1 ~ 46 미만의 임의의 값 생성 (정수)
# print(randint(1,45)) # 1 ~ 45 이하의 임의의 값 생성

###########################################################

# # 리스트 []
# # 지하철 칸별로 10명, 20명, 30명
# subway1 = 10
# subway2 = 20
# subway3 = 30

# subway = [10,20,30]
# print(subway)

# subway = ["유재석", "조세호","박명수"]
# print(subway)

# # 조세호씨가 몇번째 칸에 타고 있는지
# print(subway.index("조세호"))

# # 하하가 다음 정류장에서 다음칸에 탐
# subway.append("하하")
# print(subway)

# # 정형돈씨를 유재석 / 조세호 사이에 태워봄
# subway.insert(1, "정형돈")
# print(subway)

# # 지하철에 있는 사람을 한명씩 뒤에서 꺼냄
# print(subway.pop())
# print(subway)

# # 같은 이름의 사람이 몇 명 있는지 확인
# subway.append("유재석")
# print(subway)
# print(subway.count("유재석"))

# # 정렬도 가능
# num_list = [5,2,4,3,1]
# num_list.sort()
# print(num_list)

# # 순서 뒤집기 기능
# num_list.reverse()
# print(num_list)

# # 모두 지우기
# num_list.clear()
# print(num_list)

# # 다양한 자료형 함께 사용
# num_list = [5,2,4,3,1]
# mix_list = ["조세호", 20, True]
# print(mix_list)

# # 리스트 확장
# num_list.extend(mix_list) # 두 리스트 하나로 합치기
# print(num_list)

###########################################################

# # 사전
# cabinet = {3: "유재석", 100: "김태호"}
# print(cabinet[3])
# print(cabinet[100])

# print(cabinet.get(3))
# print(cabinet[5]) # index 에러 (프로그램 종료)
# print(cabinet.get(5, "사용가능"))  # None 출력, + 기본값 (프로그램 진행)
# print(cabinet.get(5, "사용가능"))  # 기본값 설정 (프로그램 진행)
# print("hi")

# # 사전 자료형 안에 원하는 값이 있는지 확인
# print(3 in cabinet)
# print(5 in cabinet)

# cabinet = {"A-3": "유재석", "B-100": "김태호"}
# print(cabinet["A-3"])
# print(cabinet["B-100"])

# # 새 손님
# print(cabinet)
# # 새로운 값 추가
# cabinet["C-20"] = "조세호"
# # 기존 값 변경
# cabinet["A-3"] = "김종국"
# print(cabinet)

# # 나간 손님
# del cabinet["A-3"]
# print(cabinet)

# # key 들만 출력
# print(cabinet.keys())

# # value 들만 출력
# print(cabinet.values())

# # key, value 쌍으로 출력
# print(cabinet.items())

# # 목욕탕 폐점
# cabinet.clear()
# print(cabinet)


#############################################

# # 튜플 : 내용의 변경 및 추가가 되지 않음 (속도 list보다 빠름)

# menu = ("돈까스", "치즈까스")
# print(menu[0])
# print(menu[1])

# name = "김종국"
# age = 20
# hobby = "코딩"
# print(name, age, hobby)

# # 튜플을 활용해 한번에 값을 나눠서 넣기
# (name, age, hobby) = ("김종국", 20, "코딩")
# print(name, age, hobby)

################################################

# # 집합 (set)
# 중복 안됨, 순서 없음
# my_set = {1, 2, 3, 3, 3}
# print(my_set)

# java = {"유재석", "김태호", "양세형"}
# python = set(["유재석", "박명수"])

# 교집합 (java 와 python을 모두 할 수 있는 사람)
# print(java & python)  # 유재석
# print(java.intersection(python))  # 유재석

# 합집합 (java도 할 수 있거나 python을 할 수 있는 개발자)
# print(java | python)
# print(java.union(python))

# 차집합 (java는 할 수 있지만 python을 할 수 없는 개발자)
# print(java - python)
# print(java.difference(python))

# python 할 줄 아는 사람이 늘어남
# python.add("김태호")
# print(python)

# java를 잊어버렸어요
# java.remove("김태호")
# print(java)

#########################################################

# # 자료구조의 변경
# 커피숍

# menu = {"커피", "우유", "주스"}
# print(menu, type(menu))

# menu = list(menu)
# print(menu, type(menu))

# menu = tuple(menu)
# print(menu, type(menu))

# menu = set(menu)
# print(menu, type(menu))

####################################################

# # 추첨 기능
from random import *
# lst = [1, 2, 3, 4, 5]
# print(lst)
# # 순서 섞기
# shuffle(lst)
# print(lst)
# # 샘플로 무작위로 하나 뽑기
# print(sample(lst, 1))

users = range(1, 21)  # 1 ~ 20까지숫자르 ㄹ생성
# print(type(users))  # 타입이 range
users = list(users)  # 자료 타입 변환
# print(type(users))  # 타입이 list

print(users)
shuffle(users)
print(users)

winners = sample(users, 4)  # 4 명 중에서 1명은 치킨, 3명은 커피
print("-- 당첨자 발표 --")
print("치킨 당첨자 : {0}".format(winners[0]))
print("커피 당첨자 : {0}".format(winners[1:]))
print("-- 축하합니다 --")
