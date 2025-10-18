#Câu 1: Viết hàm để Tính diện tích tam giác
'''
Yêu cầu:
Nhập vào 3 cạnh của tam giác, kiểm tra tính hợp lệ của tam giác, Sau đó tính diện tích
theo công thức Herong:

'''
import math

# Nhập vào 3 cạnh tam giác
a = float(input("Nhập cạnh a: "))
b = float(input("Nhập cạnh b: "))
c = float(input("Nhập cạnh c: "))

# Kiểm tra tính hợp lệ của tam giác
if a + b > c and a + c > b and b + c > a:
    print("Ba cạnh tạo thành một tam giác hợp lệ.")
    
    # Công thức Hê-rông
    p = (a + b + c) / 2
    S = math.sqrt(p * (p - a) * (p - b) * (p - c))
    
    print("Chu vi p =", p*2)
    print("Nửa chu vi =", p)
    print("Diện tích tam giác S =", S)
else:
    print("Ba cạnh không tạo thành tam giác hợp lệ.")
