#Câu 2: Xử lý số trong Text File
'''
Yêu cầu:
Cho một tập tin có dữ liệu trên mỗi dòng như dưới đây:
5,6,8,9,-5
-9,5,4,7,8
6,7,8,3,6,46,7,2,-6,-7
a) Viết hàm đọc file, mỗi dòng khởi tạo thành 1 list và xuất ra màn hình
b) Xuất các số âm trên mỗi dòng ra màn hình
'''



# a) Hàm đọc file và khởi tạo list cho từng dòng
def doc_file_so(filename):
    ds = []
    try:
        with open(filename, "r", encoding="utf-8") as f:
            for dong in f:
                dong = dong.strip()  # xóa khoảng trắng dư
                if dong:  # nếu dòng không rỗng
                    # tách các phần tử bởi dấu phẩy và chuyển sang kiểu int
                    hang = [int(x) for x in dong.split(",")]
                    ds.append(hang)
    except FileNotFoundError:
        print("File không tồn tại. Vui lòng kiểm tra lại.")
    return ds


# b) Hàm xuất các số âm trên mỗi dòng
def xuat_so_am(ds):
    print("\n CÁC SỐ ÂM TRÊN MỖI DÒNG ")
    for i, hang in enumerate(ds, start=1):
        am = [x for x in hang if x < 0]
        print(f"Dòng {i}: {am if am else 'Không có số âm'}")


#  Chương trình chính
def main():
    filename = "so.txt"  # Tên file chứa dữ liệu
    ds = doc_file_so(filename)

    # Xuất danh sách sau khi đọc file
    print("DỮ LIỆU TRONG FILE ")
    for i, hang in enumerate(ds, start=1):
        print(f"Dòng {i}: {hang}")

    # Xuất các số âm trên mỗi dòng
    xuat_so_am(ds)


# Gọi chương trình chính
main()

