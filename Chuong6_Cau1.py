#Câu 1: Xử lý List
'''
Yêu cầu:
Viết chương trình cho phép:
- Khởi tạo list
- Thêm phần tử vào list
- Nhập k, kiểm tra k xuất hiện bao nhiêu lần trong list
- Tính tổng các số nguyên tố trong list
- Sắp xếp
- Xóa list
'''

# Hàm kiểm tra số nguyên tố 
def la_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


# Chương trình chính
def main():
    # Khởi tạo list rỗng
    lst = []
    print("CHƯƠNG TRÌNH XỬ LÝ LIST")

    # Thêm phần tử vào list
    n = int(input("Nhập số lượng phần tử: "))
    for i in range(n):
        x = int(input(f"Nhập phần tử thứ {i+1}: "))
        lst.append(x)

    print("\nList hiện tại:", lst)

    # Nhập k, kiểm tra k xuất hiện bao nhiêu lần
    k = int(input("\nNhập giá trị k cần kiểm tra: "))
    dem = lst.count(k)
    print(f"Giá trị {k} xuất hiện {dem} lần trong list.")

    # Tính tổng các số nguyên tố trong list
    tong_nt = sum(x for x in lst if la_so_nguyen_to(x))
    print("Tổng các số nguyên tố trong list là:", tong_nt)

    # Sắp xếp list tăng dần
    lst.sort()
    print("List sau khi sắp xếp tăng dần:", lst)

    # Xóa list
    lst.clear()
    print("List sau khi xóa:", lst)


# Gọi hàm main
main()
