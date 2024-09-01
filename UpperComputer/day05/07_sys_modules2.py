import math
import random
import random
import random
# 幂
print(math.pow(10, 2))
# 向下取整1.832156
print(math.floor(1.832156))
# 向上取整
print(math.ceil(1.832156))
print(math.ceil(1.12345))
# 四舍五入
print(round(1.832156))
print(round(1.12345))

# sin cos 30 45 60
print(math.sin(math.radians(30)))
print(math.sin(math.radians(45)))

# 随机数
print(random.randint(1, 10))

# 随机小数
print(random.random())

# 随机浮点数类型
print(random.uniform(1, 10))

# 从列表中随机获取元素
arr = ["张三","李四","王五","赵六","刘七","田八"]
print(random.choice(arr))