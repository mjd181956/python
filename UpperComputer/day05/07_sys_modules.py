import sys

#命令启动参数
print(sys.argv)
print(sys.argv[1:])
print(sys.path)


print("-------------------------time")
import time

strat = time.time()  # 事件戳，单位s,1970.1.1到现在的秒数

# 阻塞当前线程，单位s
time.sleep(1)

end = time.time()

print(f"duration: {end - strat}")

print("-------------------------datetime")
from datetime import datetime

now = datetime.now()
print(now,type(now))
print(now.year, now.month, now.day, now.hour, now.minute, now.second)

# 直接把now对象，转成目标时间日期格式
print(datetime.strftime(now, "%Y-%m-%d %H:%M:%S"))
data_str = "2020-10-10 10:10:10"
datetime.strptime(data_str, "%Y-%m-%d %H:%M:%S")
print(data_str)

print("-------------------------list")

arr = [1,4,6,8,1,12,7,5,8]
print(max(arr))
print(min(arr))
print(len(arr))
print(sum(arr))
print(type(arr))

new_arr = sorted(arr)  # ��序
