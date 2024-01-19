
print(1+1)

from datetime import datetime

now = datetime.now()
start_time1 = now.second
start_time2 = now.microsecond

print (start_time1,'.',start_time2)

sum_result = 0
for i in range(1,55000350):
    sum_result += i

print(sum_result)

end_time1 = now.second
end_time2 = now.microsecond

print(end_time1,'.',end_time2)
print(end_time1-start_time1)
print(end_time2 - start_time2)

# 스타트타임과 엔드타임사이에 시간 차이가 발생할줄 알았지만 둘이 똑같았다...