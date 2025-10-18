#Câu 11: Kiểm tra số nguyên tố.
'''
Yêu cầu:
Viết chương trình nhập vào một số, kiểm tra xem số này có phải là số nguyên tố
hay không. Hỏi người dùng có tiếp tục sử dụng hay thoát phần mềm.
'''

import math

def la_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

while True:
    # Nhập số
    try:
        n = int(input("Nhập một số nguyên: "))
    except ValueError:
        print("Vui lòng nhập số nguyên hợp lệ!")
        continue
    
    # Kiểm tra nguyên tố
    if la_so_nguyen_to(n):
        print(f"{n} là số nguyên tố.")
    else:
        print(f"{n} không phải là số nguyên tố.")

    # Hỏi tiếp tục hay thoát
    tieptuc = input("Bạn có muốn tiếp tục không? (c/k): ").lower()
    if tieptuc != "c":
        print("Thoát chương trình. Tạm biệt!")
        break
