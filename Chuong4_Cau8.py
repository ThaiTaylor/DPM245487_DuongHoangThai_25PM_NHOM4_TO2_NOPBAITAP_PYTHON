#Câu 8: Viết chương trình tính loga^x
'''
Yêu cầu:
Viết chương trình tính loga
x với a, x là các số thực nhập vào từ bàn phím, và x>0, a>0, a
!= 1.( dùng logax=lnx/lna)
'''
import math

# Nhập giá trị a và x
a = float(input("Nhập cơ số a: "))
x = float(input("Nhập số x: "))

# Kiểm tra điều kiện hợp lệ
if a > 0 and a != 1 and x > 0:
    loga_x = math.log(x) / math.log(a)
    print(f"log_{a}({x}) = {loga_x}")
else:
    print("Giá trị a và x không hợp lệ! (cần a > 0, a ≠ 1, x > 0)")
