#Câu 9: Xử lý Text File - Viết phần mềm Quản Lý sản phẩm
'''
Yêu cầu:
Viết phần mềm Quản Lý sản phẩm
Mỗi danh mục có: Mã , tên; Một danh mục có nhiều sản phẩm
Mỗi sản phẩm có: Mã, tên, đơn giá; Mỗi một sản phẩm thuộc về một danh mục.
Cho phép: lưu mới, sửa, xóa, tìm kiếm, sắp xếp, lưu và đọc Text File
'''

# PHẦN MỀM QUẢN LÝ SẢN PHẨM (Text File)


import os

FILE_NAME = "sanpham.txt"

# HÀM XỬ LÝ FILE

def doc_file():
    data = []
    if not os.path.exists(FILE_NAME):
        return data
    with open(FILE_NAME, "r", encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split(";")
            if len(parts) == 5:
                data.append({
                    "ma_dm": parts[0],
                    "ten_dm": parts[1],
                    "ma_sp": parts[2],
                    "ten_sp": parts[3],
                    "don_gia": float(parts[4])
                })
    return data

def luu_file(data):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        for sp in data:
            f.write(f"{sp['ma_dm']};{sp['ten_dm']};{sp['ma_sp']};{sp['ten_sp']};{sp['don_gia']}\n")


# HÀM CHỨC NĂNG

def hien_thi(data):
    print("\n{:<10} {:<15} {:<10} {:<20} {:<10}".format("Mã DM", "Tên Danh Mục", "Mã SP", "Tên SP", "Đơn Giá"))
    print("-" * 70)
    for sp in data:
        print("{:<10} {:<15} {:<10} {:<20} {:<10}".format(
            sp["ma_dm"], sp["ten_dm"], sp["ma_sp"], sp["ten_sp"], sp["don_gia"]
        ))

def them_san_pham(data):
    ma_dm = input("Nhập mã danh mục: ")
    ten_dm = input("Nhập tên danh mục: ")
    ma_sp = input("Nhập mã sản phẩm: ")
    ten_sp = input("Nhập tên sản phẩm: ")
    don_gia = float(input("Nhập đơn giá: "))
    data.append({
        "ma_dm": ma_dm,
        "ten_dm": ten_dm,
        "ma_sp": ma_sp,
        "ten_sp": ten_sp,
        "don_gia": don_gia
    })
    luu_file(data)
    print("Đã thêm sản phẩm và lưu vào file.")

def sua_san_pham(data):
    ma_sp = input("Nhập mã sản phẩm cần sửa: ")
    for sp in data:
        if sp["ma_sp"] == ma_sp:
            sp["ten_sp"] = input("Tên sản phẩm mới: ")
            sp["don_gia"] = float(input("Đơn giá mới: "))
            luu_file(data)
            print("Đã cập nhật sản phẩm.")
            return
    print("Không tìm thấy sản phẩm!")

def xoa_san_pham(data):
    ma_sp = input("Nhập mã sản phẩm cần xóa: ")
    for sp in data:
        if sp["ma_sp"] == ma_sp:
            data.remove(sp)
            luu_file(data)
            print("Đã xóa sản phẩm.")
            return
    print("Không tìm thấy sản phẩm!")

def tim_kiem(data):
    tu_khoa = input("Nhập tên hoặc mã cần tìm: ").lower()
    kq = [sp for sp in data if tu_khoa in sp["ten_sp"].lower() or tu_khoa in sp["ma_sp"].lower()]
    if kq:
        hien_thi(kq)
    else:
        print("Không tìm thấy sản phẩm!")

def sap_xep(data):
    data.sort(key=lambda x: x["don_gia"], reverse=True)
    hien_thi(data)


# HÀM MAIN MENU

def menu():
    data = doc_file()
