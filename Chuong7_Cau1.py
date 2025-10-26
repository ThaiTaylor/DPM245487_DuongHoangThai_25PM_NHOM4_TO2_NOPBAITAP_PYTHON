#Câu 1: Quản lý Sản phẩm- Text File
'''
Yêu cầu:
Viết chương trình nhập vào thông tin của một sản phẩm:
Mã: Chuỗi
Tên: Chuỗi
Đơn Giá: Số
Mỗi một Sản phẩm sau khi nhập thành công sẽ lưu nối đuôi vào File theo quy tắc:
MSSP;Tên Sản phẩm; Đơn giá
Mẫu Dữ liệu lưu nối đuôi vào file tương tự như dưới đây:
sv1;Cocacolala;15.5
sp2;Bưởi 5 Roi;18.0
sp3;Bia 333;14.5
Sau đó thực hiện 2 chức năng chính:
a) xuất danh sách sản phẩm từ File
b) Sắp xếp Sản phẩm theo đơn giá giảm dần
'''



# Hàm ghi sản phẩm vào file
def ghi_san_pham(filename):
    with open(filename, "a", encoding="utf-8") as f:
        ma = input("Nhập mã sản phẩm: ")
        ten = input("Nhập tên sản phẩm: ")
        gia = float(input("Nhập đơn giá: "))
        f.write(f"{ma};{ten};{gia}\n")
    print("Đã lưu sản phẩm thành công!\n")

#  Hàm đọc danh sách sản phẩm từ file
def doc_danh_sach(filename):
    ds = []
    try:
        with open(filename, "r", encoding="utf-8") as f:
            for dong in f:
                dong = dong.strip()
                if dong:  # nếu dòng không rỗng
                    ma, ten, gia = dong.split(";")
                    ds.append([ma, ten, float(gia)])
    except FileNotFoundError:
        print("File chưa tồn tại. Vui lòng thêm sản phẩm trước.")
    return ds

#  Hàm xuất danh sách sản phẩm
def xuat_danh_sach(ds):
    if not ds:
        print("Danh sách rỗng!")
    else:
        print("\nDANH SÁCH SẢN PHẨM ")
        print(f"{'Mã':<10}{'Tên sản phẩm':<20}{'Đơn giá'}")
        for ma, ten, gia in ds:
            print(f"{ma:<10}{ten:<20}{gia:.2f}")

#  Hàm sắp xếp theo đơn giá giảm dần
def sap_xep_theo_gia(ds):
    return sorted(ds, key=lambda sp: sp[2], reverse=True)

#  Chương trình chính
def main():
    filename = "sanpham.txt"
    while True:
        print("\n MENU QUẢN LÝ SẢN PHẨM")
        print("1. Nhập thêm sản phẩm")
        print("2. Xuất danh sách sản phẩm")
        print("3. Sắp xếp theo đơn giá giảm dần")
        print("0. Thoát")
        chon = input("Chọn chức năng: ")

        if chon == "1":
            ghi_san_pham(filename)
        elif chon == "2":
            ds = doc_danh_sach(filename)
            xuat_danh_sach(ds)
        elif chon == "3":
            ds = doc_danh_sach(filename)
            ds_sx = sap_xep_theo_gia(ds)
            print("\nDANH SÁCH SAU KHI SẮP XẾP GIẢM DẦN THEO GIÁ")
            xuat_danh_sach(ds_sx)
        elif chon == "0":
            print("Cảm ơn bạn đã sử dụng chương trình!")
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng chọn lại!")

# Gọi chương trình chính
main()
