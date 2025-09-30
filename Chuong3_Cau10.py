#Câu 10: Tính dãy số.
'''
Yêu cầu:
Cho biểu thức toán học sau:
Tinh S (x,n) = x + x^2/2! + x^3/3! + ... + x^n/n!
Viết chương trình cho phép nhập x, n và xuất ra kết quả của biểu thức.
'''

x = float(input("Nhập x: "))
n = int(input("Nhập n: "))

S = 0
gt = 1   # lưu giai thừa, ban đầu là 1 (0! = 1)

for i in range(1, n + 1):
    gt *= i          # cập nhật giai thừa i!
    S += x**i / gt   # cộng dồn vào tổng

print("Kết quả S =", S)


#Hoặc cũng có thể viết như sau (dùng math.factorial() thay vì tính giai thừa cơ bản).
'''
import math

# Nhập dữ liệu
x = float(input("Nhập x: "))
n = int(input("Nhập n: "))

# Tính tổng
S = 0
for i in range(1, n + 1):
    S += x**i / math.factorial(i)

# Xuất kết quả
print(f"S({x}, {n}) = {S}")

'''