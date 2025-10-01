#Câu 19: Tính giá trị biểu thức S
import math

def S_factorial(x, n):
    s = 0.0
    for k in range(n+1):
        t = x**(2*k+1)
        d = math.factorial(2*k+1)
        s += t / d
    return s

# Ví dụ:
x = float(input("Nhập x: "))
n = int(input("Nhập n: "))
print("S =", S_factorial(x, n))
