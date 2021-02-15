# print(abs(-5)) # 5
# print((pow(4,2))) # 4^2 = 4*4 = 16
# print(max(5,12)) # 12
# print(min(5,12)) # 5
# print(round(3.24)) # 3
# print(round(4.99)) # 5

# from math import *
# print(floor(4.99)) # 내림 4
# print(ceil(3.14)) # 올림 4
# print(sqrt(16)) # 제곱근 4

# from random import *
# print(random()) # 0.0 ~ 1.0 미만의 임의의 값 생성
# print(randrange(1,46)) # 1 ~ 46 미만의 임의의 값 생성
# print(randint(1,45)) # 1 ~ 45 이하의 임의의 값 생성

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

# # 하하씨가 다음 정류장에서 다음칸에 탐
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
# num_list.extend(mix_list)
# print(num_list)

# 사전
cabinet = {3: "유재석", 100: "김태호"}
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))
# print(cabinet[5]) # index 에러 (프로그램 종료)
print(cabinet.get(5, "사용가능"))  # None 출력, + 기본값 (프로그램 진행)
print(cabinet.get(5, "사용가능"))  # 기본값 설정 (프로그램 진행)
print("hi")
