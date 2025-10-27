#Câu 2: Xử lý List nhập ngẫu nhiên
'''
Yêu cầu:
Viết chương trình cho phép:
- Viết lệnh khởi tạo ngẫu nhiên n phần tử cho list
- Gọi k là một số nhập từ bàn phím, hãy xóa tất cả các phần tử có giá trị k tồn tại
trong list
- Kiểm tra list có đối xứng hay không
'''

import random

def la_doi_xung(lst):
    """Hàm kiểm tra list có đối xứng không"""
    return lst == lst[::-1]

def main():
    print("CHƯƠNG TRÌNH XỬ LÝ LIST NGẪU NHIÊN")
    
    # Khởi tạo list ngẫu nhiên n phần tử
    n = int(input("Nhập số lượng phần tử n: "))
    lst = [random.randint(0, 9) for _ in range(n)]  # tạo list gồm n số ngẫu nhiên từ 0-9
    print("List ngẫu nhiên:", lst)

    # Nhập k và xóa tất cả phần tử có giá trị bằng k
    k = int(input("Nhập giá trị k cần xóa: "))
    lst = [x for x in lst if x != k]  # giữ lại các phần tử khác k
    print("List sau khi xóa các phần tử =", k, "là:", lst)

    # Kiểm tra list có đối xứng hay không
    if la_doi_xung(lst):
        print("List là đối xứng.")
    else:
        print("List KHÔNG đối xứng.")

#  Gọi hàm main 
main()
