#Câu 9: Viết chương trình tính căn bậc 2 lồng nhau
import math

# Nhập n
n = int(input("Nhập số n: "))

# Tính S(n)
s = math.sqrt(2)
for i in range(1, n):
    s = math.sqrt(2 + s)

# Xuất kết quả
print(f"S({n}) = {s}")
