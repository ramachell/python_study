import time

start_time = time.time()
print(start_time)

sum_result = 0
for i in range(1,55000350):
    sum_result += i

print(sum_result)

end_time = time.time()
print(end_time)

print(end_time-start_time)

# time.time()을 하니 정상적으로 측정됐다
# 여기서 알아보고 싶었던것 sum과 for문을 통한 시간차이 비교
print("------------------")

start_time = time.time()
print(start_time)

sum_result = 0
sum_result = sum(range(1,55000350))
print(sum_result)

end_time = time.time()
print(end_time)

print(end_time-start_time)
