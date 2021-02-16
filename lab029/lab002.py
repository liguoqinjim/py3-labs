import decimal
from decimal import Decimal

context = decimal.getcontext()  # 获取decimal现在的上下文
context.rounding = decimal.ROUND_05UP
# 修改舍入方式为四舍五入
decimal.getcontext().rounding = "ROUND_HALF_UP"

print(round(Decimal(2.55), 1))  # 2.6
print(format(Decimal(2.55), '.1f'))  # '2.6'

# 测试
print(round(Decimal(0.55), 1))  # 2.6
print(round(Decimal(1.55), 1))  # 2.6
print(round(Decimal(2.55), 1))  # 2.6

print(round(0.5, 1))
print(round(1.5, 1))

#
print("6位")
print(round(Decimal(0.0095588235), 6))
print(format(Decimal(0.0095588235), '.6f'))  # '2.6'

from decimal import Decimal

