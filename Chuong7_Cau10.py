#Câu 10: Xử lý JSON File - Viết phần mềm Quản Lý Sinh Viên
'''
Yêu cầu:
Viết phần mềm quản lý Sinh Viên
Mỗi một lớp có: Mã lớp, tên; một lớp có nhiều Sinh viên
Mỗi sinh viên có: mã, tên, năm sinh; Mỗi một sinh viên thuộc về một lớp.
Cho phép: lưu mới, sửa, xóa, tìm kiếm, sắp xếp, lưu và đọc JSon File

'''

# PHẦN MỀM QUẢN LÝ SINH VIÊN (JSON FILE)


import json
import os

FILE_NAME = "sinhvien.json"


# HÀM XỬ LÝ FILE

def doc_file():
    if not os.path.exists(FILE_NAME):
        return {"lop": []}
    with open(FILE_NAME, "r", encoding="utf-8") as f:
        return json.load(f)

def luu_file(data):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print("Dữ liệu đã được lưu vào file JSON.")


# HÀM XỬ LÝ SINH VIÊN & LỚP

def hien_thi(data):
    print("\nDANH SÁCH LỚP & SINH VIÊN")
    for lop in data["lop"]:
        print(f"\nLớp: {lop['ma_lop']} - {lop['ten_lop']}")
        if not lop["sinh_vien"]:
            print("   (Chưa có sinh viên)")
        else:
            print("{:<10} {:<25} {:<10}".format("Mã SV", "Tên Sinh Viên", "Năm Sinh"))
            print("-" * 50)
            for sv in lop["sinh_vien"]:
                print("{:<10} {:<25} {:<10}".format(sv["ma_sv"], sv["ten_sv"], sv["nam_sinh"]))

def them_lop(data):
    ma_lop = input("Nhập mã lớp: ")
    ten_lop = input("Nhập tên lớp: ")
    data["lop"].append({"ma_lop": ma_lop, "ten_lop": ten_lop, "sinh_vien": []})
    luu_file(data)

def them_sinh_vien(data):
    ma_lop = input("Nhập mã lớp mà sinh viên thuộc về: ")
    lop = next((l for l in data["lop"] if l["ma_lop"] == ma_lop), None)
    if lop:
        ma_sv = input("Nhập mã sinh viên: ")
        ten_sv = input("Nhập tên sinh viên: ")
        nam_sinh = int(input("Nhập năm sinh: "))
        lop["sinh_vien"].append({"ma_sv": ma_sv, "ten_sv": ten_sv, "nam_sinh": nam_sinh})
        luu_file(data)
    else:
        print("Không tìm thấy lớp!")

def sua_sinh_vien(data):
    ma_sv = input("Nhập mã sinh viên cần sửa: ")
    for lop in data["lop"]:
        for sv in lop["sinh_vien"]:
            if sv["ma_sv"] == ma_sv:
                sv["ten_sv"] = input("Tên mới: ")
                sv["nam_sinh"] = int(input("Năm sinh mới: "))
                luu_file(data)
                print("Đã cập nhật sinh viên.")
                return
    print("Không tìm thấy sinh viên!")

def xoa_sinh_vien(data):
    ma_sv = input("Nhập mã sinh viên cần xóa: ")
    for lop in data["lop"]:
        for sv in lop["sinh_vien"]:
            if sv["ma_sv"] == ma_sv:
                lop["sinh_vien"].remove(sv)
                luu_file(data)
                print("Đã xóa sinh viên.")
                return
    print("Không tìm thấy sinh viên!")

def tim_kiem(data):
    tu_khoa = input("Nhập tên hoặc mã sinh viên cần tìm: ").lower()
    kq = []
    for lop in data["lop"]:
        for sv in lop["sinh_vien"]:
            if tu_khoa in sv["ma_sv"].lower() or tu_khoa in sv["ten_sv"].lower():
                kq.append((lop["ma_lop"], sv))
    if kq:
        print("\nKẾT QUẢ TÌM KIẾM:")
        print("{:<10} {:<10} {:<25} {:<10}".format("Lớp", "Mã SV", "Tên SV", "Năm Sinh"))
        print("-" * 60)
        for lop_ma, sv in kq:
            print("{:<10} {:<10} {:<25} {:<10}".format(lop_ma, sv["ma_sv"], sv["ten_sv"], sv["nam_sinh"]))
    else:
        print("Không tìm thấy sinh viên!")

def sap_xep(data):
    for lop in data["lop"]:
        lop["sinh_vien"].sort(key=lambda x: x["ten_sv"])
    luu_file(data)
    print("Đã sắp xếp sinh viên theo tên trong từng lớp.")


# MENU CHÍNH

def menu():
    data = doc_file()
    while True:
        print("\nQUẢN LÝ SINH VIÊN")
        print("1. Xem danh sách lớp & sinh viên")
        print("2. Thêm lớp")
        print("3. Thêm sinh viên")
        print("4. Sửa sinh viên")
        print("5. Xóa sinh viên")
        print("6. Tìm kiếm sinh viên")
        print("7. Sắp xếp sinh viên theo tên")
        print("0. Thoát")
        chon = input("Chọn chức năng: ")

        if chon == "1":
            hien_thi(data)
        elif chon == "2":
            them_lop(data)
        elif chon == "3":
            them_sinh_vien(data)
        elif chon == "4":
            sua_sinh_vien(data)
        elif chon == "5":
            xoa_sinh_vien(data)
        elif chon == "6":
            tim_kiem(data)
        elif chon == "7":
            sap_xep(data)
        elif chon == "0":
            print("Cảm ơn bạn đã sử dụng chương trình!")
            break
        else:
            print("Lựa chọn không hợp lệ!")


# CHẠY CHƯƠNG TRÌNH

menu()
