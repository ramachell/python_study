# 1 ------------------------------------------------------------------------------
print("Hello World")

print("Mary's cosmetics")

print('"도둑이야"')

print("C:\Windows")

print("안녕하세요. \n만나서\t\t반갑습니다")
# \n은 줄 한칸내림, \t는 탭 1번

print("오늘은", "일요일")

print("naver;kakao;sk;samsung")
print("naver", "kakao", "sk", "samsung", sep=";")

print("naver", "kakao", "sk", "samsung", sep="/")

print("first", end="")
print("second")

print(5 / 3)

# 11 ------------------------------------------------------------------------------
삼성전자 = 50000
총평가금액 = 삼성전자 * 10
print(총평가금액)

시가총액 = 298000000000000
현재가 = 50000
PER = 15.79

print(시가총액, type(시가총액))
print(현재가, type(현재가))
print(PER, type(PER))

s = "hello"
t = "python"
print(s + "!", t)

print(2 + 2 * 3)

a = 128
print(type(a))

a = "132"
print(type(a))

num_str = "720"
print(num_str)
print(int(num_str))

num = 100
print(num, type(num))
print(str(num), type(str(num)))

num = "15.79"
print((float(num)), type(num), type(float(num)))

year = "2020"
print(int(year) - 3)
print(int(year) - 2)
print(int(year) - 1)

month_cost = 48584
total_month = 36
print(month_cost * total_month)

# 21----------------------------------------------------

letters = "python"
print(letters[0], letters[2])

license_plate = "24가 2210"
print(license_plate[-4:])

str = "1234567890"
print(str[-3 : len(str)])

string = "홀짝홀짝홀짝"
print(string[::2])
print(str[::2])

string = "PYTHON"
print(string[::-1])

phone_number = "010-2222-1111"
print(phone_number.replace("-", "_"))

print(phone_number.replace("-", ""))

lang = "python"
# lang[0] = 'P'
print(lang)

name1 = "asdf"
name2 = "qwer"
age1 = 10
age2 = 13

print("이름: %s 나이: %d" % (name1, age1))
print("이름: %s 나이: %d" % (name2, age2))

print("이름: {} 나이: {}".format(name1, age1))
print("이름: {} 나이: {}".format(name2, age2))

print(f"이름: {name1} 나이: {age1}")
print("이름: {} 나이: {}".format(name2, age2))


file_name = "보고서.xlsx"
file_name.endswith("xlsx")

a = "hello world"
b = a.split()
print(a)
print(b, type(b))

movie_rank = [11, "22", "33"]
print(movie_rank)

movie_rank.insert(2, "555")

lang1 = ["C", "C++", "JAVA"]
lang2 = ["Python", "Go", "C#"]

lang3 = lang1 + lang2
print(lang3)

max(lang3)

# sum(lang3)

num = ["aa", "bb"]
# sum(num)

nums = num[0] + num[1]
print(nums)

cook = [
    "피자",
    "김밥",
    "만두",
    "양념치킨",
    "족발",
    "피자",
    "김치만두",
    "쫄면",
    "소시지",
    "라면",
    "팥빙수",
    "김치전",
]

print(len(cook))

nums = [1, 2, 3, 4, 5]
sum(nums) / len(nums)

interest = ["삼성전자", "LG전자", "Naver"]
print(interest[0], interest[2])
print(interest[::2])

interest = ["삼성전자", "LG전자", "Naver", "SK하이닉스", "미래에셋대우"]
print(" ".join(interest))

print("/".join(interest))

print("\n".join(interest))

string = "삼성전자/LG전자/Naver"
interest = string.split("/")
print(interest)

data = [2, 4, 3, 1, 5, 10, 9]
print(data.sort())
# sort()는 원래의 data를 변경하고 return 은 None임
print(data)

data = sorted(data)
print(data)

tuples = ()
print(tuples, type(tuple))

tuples = 1
print(tuples, type(tuple))
# 1개만 저장할시 튜플이 안만들어짐

tuples = (1,)
print(tuples, type(tuple))

t = (1, 2, 3)
# t[0] = 'a'

t = 1, 2, 3, 4
print(t, type(t))
# 편의상 괄호없이 위처럼 해도 튜플됨

t = "a", "b", "c"
# t[0] = 'A' 불가능 튜플은 값변경 안됨 아예 새로 정의해야함
t = "A", "b", "c"

interest = ("삼성전자", "LG전자", "SK Hynix")
interest = list(interest)
print(interest)

temp = ("apple", "banana", "cake")
a, b, c = temp
print(a, b, c)
type(a)
# str

data = tuple(range(2, 100, 3))
print(data)

data = tuple(range(2, 100, 2))
print(data)
# tuple 라는 변수를 쓰게되면 tuple()는 함수가 아니라 변수로서 호출되게됨 변수이름을 정핼때 주의할것!!!

scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
*valid_score, _, _ = scores
print(valid_score)

scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
_, _, *valid_score = scores
print(valid_score)

ice = {"메로나": 1000, "폴라포": 1200, "빵빠레": 1800}
print(ice)

ice = {"메로나": (300, 20), "비비빅": (400, 3), "죠스바": (250, 100)}
print(ice["메로나"])

print(ice.keys())

ice = list(ice.keys())
print(ice)

date = ["09/05", "09/06", "09/07", "09/08", "09/09"]
close_price = [10500, 10300, 10100, 10800, 11000]

result = dict(zip(date, close_price))
print(result)

aaa = bool(True)
print(aaa)

x = 4
print(5 > x > 1)

print(3 >= 4)


if 4 < 3:
    print("Hello World.")
else:
    print("Hi, there.")

user = input("입력:")
print(user * 2)

num = input("숫자를 입력하세요 : ")
print(num)

num = 40


def isEven(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"


print(isEven(num))

fruit = ["사과", "포도", "홍시"]

user = input("과일 말해봐 : ")
if user in fruit:
    print("정답")
else:
    print("떙")

fruit = {"봄": "딸기", "여름": "토마토", "가을": "사과"}
user = "봄"
user2 = "딸기"


def fruitTest(user):
    if user in fruit:
        print("답")
    else:
        print("땡")


fruitTest(user)
fruitTest(user2)

# in 에서 딕셔너리를 넣을시 keys()를 생략해도 된다
# 위에서 fruit.keys() == fruit


def reverseUpperLower(str):
    if str.islower():
        print(str.upper())
    else:
        print(str.lower())


reverseUpperLower("A")
reverseUpperLower("a")

score = 12

if 81 <= score <= 100:
    print("grade is A")
elif 61 <= score <= 80:
    print("grade is B")
elif 41 <= score <= 60:
    print("grade is C")
elif 21 <= score <= 40:
    print("grade is D")
elif score <= 20:
    print("grade is 사람이냐")


num1 = 10
num2 = 9
num3 = 20

print(max(num1, num2, num3))

num = "011-222-3333"
num = num[:3]
print(num)

num = "822222-3020203"
num2 = "822222-2020203"

if num[7] == "1" or "3":
    print("남자")
else:
    print("여자")


num = "901010-1021204"
nums = [2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5]


def isP(num):
    num1 = num.replace("-", "")
    num2 = num1[0:-1]
    result = 0
    for i, j in zip(num2, nums):
        result = result + int(i) * j
        print(result)
    print("last num", 11 - result % 11)
    if int(num[-1:]) == (11 - result % 11):
        return True
    else:
        return False


print(isP(num))


list1 = ["intra.h", "intra.c", "define.h", "run.py"]

for name in list1:
    if name.endswith("h"):
        print(name)

print(list(range(0, 31, 3)))

result = 1
for i in range(1, 11):
    result *= i
print(result)

my_list = ["가", "나", "다", "라", "마"]

for i in range(len(my_list) - 2):
    print(my_list[i], my_list[i + 1], my_list[i + 2])


print(my_list[0], my_list[1])
print(my_list[1])
print(my_list[2])
print(my_list[3])
print(my_list[4])

print("aaa" + 2)


def print_keys(dic):
    for i in dic.keys():
        print(i)


print_keys({"이름": "김말똥", "나이": 30, "성별": 0})

diccc = {"이름": "김말똥", "나이": 30, "성별": 0}
print(diccc.keys())


def print_5xn(line):
    chunk_num = int(len(line) / 5)
    for x in range(chunk_num + 1):
        print(line[x * 5 : x * 5 + 5])


print_5xn("아이엠어보이유알어걸s")

print(int(2323.9))


def my_print(a, b):
    print("왼쪽:", a)
    print("오른쪽:", b)


my_print(a=100, b=200)

my_print(d=100, e=200)

result = 0


def n_plus_1(n):
    result = n + 1


n_plus_1(3)
print(result)


def make_list(str):
    print(list(str))


make_list("abcd")


def convert_int(str):
    return int(str.replace(",", ""))


print(convert_int("1,234,567"))

import datetime

now = datetime.datetime.now()

for day in range(5, 0, -1):
    delta = datetime.timedelta(days=day)
    date = now - delta
    print(date)

print(list(range(0, 4, 0.1)))


class Human:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def who(self):
        print("이름 : " + self.name + "age : " + self.age + "gender : " + self.gender)


baddd = Human("rism", 28, "Female")

baddd.who()


class Human:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def who(self):
        print("이름: {} 나이: {} 성별: {}".format(self.name, self.age, self.sex))


areum = Human("아름", 25, "여자")
areum.who()  # Human.who(areum)


class OMG:
    def print2():
        print("Oh my god")


mystock = OMG()
mystock.print2()  # OMG.print(mystock)


class Stock:
    def __init__(self, name, price, code, per: float, pbr: float, money_rate: float):
        self.name = name
        self.price = price
        self.code = code
        self.per = per
        self.pbr = pbr
        self.money_rate = money_rate

    def set_name(self, name):
        self.name = name

    def set_code(self, price):
        self.price = price

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price


samsung = Stock("삼성", 120000)

print(samsung.name)
print(samsung.price)

a = Stock(None, None)
a.name
a.set_name("A")
a.name

a.get_name()

samsung.get_name()
samsung.get_price()

lg = Stock("lg",40000,"302030",15.79,1.33,2.83)
lg.money_rate

samsung = Stock("삼성",2000,"0303021",15.79,1.33,2.83)
hyundai = Stock("현대",100,"005380",8.70,0.35,4.27)

stock_list = []

stock_list.append(samsung)
stock_list.append(lg)
stock_list.append(hyundai)

print(stock_list)

for i in stock_list:
    print(i.name," : ", i.code)
    print(i.name," : ",i.per)

import random

class Account():
    account_count = 0

    def __init__(self,name,balance):
        self.deposit_log =[]
        self.deposit_count = 0 
        self.name = name
        self.balance = balance
        self.bank = "SC Bank"
        self.account_number = str(random.randint(0,999)).zfill(3) + "-" + str(random.randint(0,99)).zfill(2) + "-" + str(random.randint(0,999999)).zfill(6)
        Account.account_count += 1

    def get_account_num(cls):
        print(cls.account_count)

    def deposit(self,insert):
        if(insert >= 1):
            self.balance += insert
            self.deposit_count += 1
            self.deposit_log.append(insert)
            if(self.deposit_count % 5 == 0):
                self.balance = self.balance*1.01 
        print(self.balance)

maee = Account("maee",1000000000000)
maee.account_number

print(Account.account_count)

maee.get_account_num()

badel = Account("badel",10000)

badel.deposit(12)
badel.deposit(15)
badel.deposit(17)
badel.deposit(13)
badel.deposit(1123)
badel.deposit_count

badel.deposit_log

rere = 123456789
print("money : " , f"{2000000:,}")
print("money : ",f"{rere:,}")

class car():
    def __init__(self,wheel,price) -> None:
        self.wheel = wheel
        self.price = price

car1 = car(2,10000)

car1.wheel
car1.price

class bicycle(car):
    def __init__(self, wheel, price,gear) -> None:
        super().__init__(wheel, price)
        self.gear = gear
    
    def get_info(self):
        print("wheel : ",self.wheel)
        print("price : ",self.price)

bicycle1 = bicycle(2,1000,"si")

bicycle1.wheel
bicycle1.price
bicycle1.gear
bicycle1.get_info()

class 부모:
    def 호출(self):
        print("부모호출")

class 자식(부모):
    def 호출(self):
        print("자식호출")


나 = 자식()
나.호출()

class 부모:
    def __init__(self):
        print("부모생성")

class 자식(부모):
    def __init__(self):
        print("자식생성")

나 = 자식()


class 부모:
  def __init__(self):
    print("부모생성")

class 자식(부모):
  def __init__(self):
    print("자식생성")
    super().__init__()

나 = 자식()

import csv

f = open ("examp.txt",mode="wt",encoding="utf-8")
f.write("393223\n")
f.write("393224\n")
f.write("393225\n")
f.close()

f = open("example.csv",mode="wt",encoding="cp949")
writer = csv.writer(f)

list1 = ["name","code","per"]
list2 = ["sam","111","1.2"]
list3 = ["lg","222","1.5"]

writer.writerow(list1)
writer.writerow(list2)
writer.writerow(list3)
f.close()

f = open("examp.txt",encoding="utf-8")
lines = f.readlines()

print(lines)

codes=[]
for line in lines:
    code = line.strip()
    codes.append(code)

print(codes)

computer1 = 13
computer2 = 18
computer3 = 11

program = [11,2,1,3,5,7,8,9,13,22,11,44,33,22,14,15,41,32]

def sol(com1,com2,com3,pro):
    pro.sort(reverse=True)
    


program.sort(reverse=True)
print(program)


# 각 자리의 합을 for 로
def sum1(num):
    result = 0
    for i in range(len(str(num))):
        result += int(str(num)[i])
        print(result)

sum1(39302)

# 재귀함수로
def sum2(num):
    if(num==0):
        return 0
    else:
        return num % 10 + sum2(num//10)
    
sum2(12391232333)

f = open("examp.txt",encoding="utf-8")
lines = f.readlines()

data = {}
for line in lines:
    line = line.strip()
    k, v = line.split()
    print(k,v)
    data[k] = v

print(data)
f.close()


per = ["10.31", "", "8.00"]

for i in per:
    try:
        print(float(i))
    except:
        print(0)

new_per = []
for i in per:
    try:
        new_per.append(float(per[i]))
    except:
        new_per.append(0)

print(new_per)

from functools import reduce 

# reduce
# y엔 list의 문자하나를 넣고 x엔 그 결과가 저장됨
# 1 : x에 첫번째, y에 두번째가 들어감 -> y+x = ba
# 2 : 여기부터 좀 다른데 y = 세번째인 c , x = ba가 들어감 고로 c+ba = cba
# 3 .....
# 4 : y = e , x = dcba y+x = edcda
reduce(lambda x, y: y + x, 'abcde')

reduce(lambda x, y: print(y,x), 'abcde')

reduce(lambda x, y: print(y,x), [1,2,3,4,5,6])

(lambda x,y: x + y)(10, 20)


def read(text):
    # 이곳에 코드를 작성하세요.
    
    return ridename, cmmin, cmmax



ridename, cmmin, cmmax = read(input())
print("이름:", ridename)
print("하한:", cmmin)
print("상한:", cmmax)
num=2
print("I {} ddd {}".format(10,num))

tt = 1,2,3,4,5,6,7

class Fam():
    lala = "ddd"

famm = Fam()
famm2 = Fam()
famm3 = Fam()

famm.lala
famm2.lala


famm.lala = "a"


Fam.lala="D"

import mod1

def gugu(n):
    print(n*n)

gugu(3)