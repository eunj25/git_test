from datetime import datetime
import random


x = input("첫번째 숫자를 입력해주세요>> ")
y = input("두번째 숫자를 입력해주세요>> ")
bob = int(x)*int(y)
print(bob)

# ==============================================

year = input("태어난 연도를 입력하세요>> ")
now = datetime.now()

age = now.year - int(year) + 1

print(str(age) + "살 입니다.")

# =====================조건문 예제 01

money = int(input("지금 얼마 가지고 있나요?>> "))

if money >= 20000:
  print("치킨에 맥주를 추천합니다.")
elif money >= 10000:
  print("돈가스를 추천합니다.")
else:
  print("편의점 가세요ㅎ")

# =====================조건문 예제 02

price = int(input("현재 가격이 얼마입니까?>> "))

if price >= 90000:
  print("매도합니다.")
elif price >= 80000:
  print("대기중입니다.")
else: 
  print("매수합니다.")

# =====================조건문 예제 03

bag = int(input("가방의 금액을 입력해주세요.>> "))
watch = int(input("시계의 금액을 입력해주세요.>> "))

total = bag + watch

if total >= 100000:
  total = (total*0.7)
elif total >= 50000:
  total = (total*0.8)
else:
  total = (sum*0.9)

print("합계 할인 금액은" + str(total) + "입니다.")



#  반복문 예제 01=======================
names = ['상욱', '상후', '은주']

for name in names:
  if name == '상욱':
    print(name + '은 강아지입니다.')
  elif name == '상후':
    print(name + '는 남성입니다.')
  else:
    print(name + '는 여성입니다.')

#  반복문 예제 02=======================
for i in range(1, 11):
  print(i, '는 정수입니다')

count = 0
while count <= 5:
  print(count,'번째 반복입니다.')
  count = count + 1

#  반복문 예제 03=======================
numder = int(input("정수를 입력해주세요. >> "))
num_sum = 0

for num in range(1, numder+1):
  num_sum += num

print(num_sum)

#  반복문 예제 04 =======================
print("프로그램 시작")

# num = int(input("종료하려면 -1를 입력하세요. >> "))

# while num != -1:
#   num = int(input("종료하려면 -1를 입력하세요. >> "))

while True:
  num = int(input("종료하려면 -1를 입력하세요. >> "))
  if num == -1:
    break

print("프로그램 종료")

#  반복문 예제 05=======================
while True:
  print("메뉴를 입력하세요")
  menu = int(input("1. 게임시작 2. 랭킹보기 3. 게임종료 >>"))

  if menu == 1:
    print("-> 게임을 시작합니다.")
  elif menu == 2:
    print("-> 랭킹보기")
  elif menu == 3:
    print("-> 게임을 종료합니다.")
    break
  else:
    print("-> 다시 입력하세요.")

#  반복문 예제 06 별 그리기=======================
for i in range(1, 6): # 1-5순서열
  print('*' * i)

for i in range(1, 6): # 1-5순서열
  print('*' * (6-i))

for i in range(1, 6): # 1-5순서열
  print(' ' * (5-i) + '*' * i)

for i in range(1, 6): # 1-5순서열
  print(' ' * (i-1) + '*' * (6-i))


# 함수 =======================
def getRandomNumber():
  numder = random.randint(1,10)
  return numder
  
print(getRandomNumber())

# 함수예제01 =======================
def getRandomNumber():
  numder = random.randint(1,45)
  return numder

lottoList = []
count = 0 

while True:
    if count > 5:
      break

    lottoNum = getRandomNumber()
    
    if lottoNum not in lottoList:  # 중복제거
      lottoList.append(lottoNum)
      count = count + 1
  
print(lottoList)

# =======================딕셔너리 
play_data = {
   'result' : '승리',
   'name' : 'wukk',
   'kill' : 9,
   'death' : 5,
   'assist' : 15
}
for key in play_data.keys():
   print(key)

for value in play_data.values():
   print(value)

for key,value in play_data.items():
   print(key,value)
   
# =======================튜플
# 값을 변경할 수 없는 리스트

# =======================클래스
class Monster:
   def __init__(self, name, age):
      self.name = name
      self.age = age
   
   def say(self):
      print(f'나는 {self.name}, {self.age}살 이다')

shark = Monster("상어",8)
shark.say()