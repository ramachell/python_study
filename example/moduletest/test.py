from moduletest.sound import *

echo.echo_test()

4/0
try:
    4/0
except ZeroDivisionError as e:
    print(e,"에러나자나")


try:
    4/0
except Exception as e :
    print(e)

import random

ran = random()

ran.ranint(1,3)
random.randint(1,3)