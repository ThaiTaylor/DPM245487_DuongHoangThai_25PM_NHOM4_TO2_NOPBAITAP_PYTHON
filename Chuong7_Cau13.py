#Câu 13: Xử lý XML File - Viết phần mềm Quản Lý Thiết Bị

from xml.dom import minidom

# =======================
# 1. Đọc danh sách nhóm
# =======================
def doc_nhom(file_xml):
    print("=== DANH SÁCH NHÓM THIẾT BỊ ===")
    doc = minidom.parse(file_xml)
    nhoms = doc.getElementsByTagName("nhom")

    ds_nhom = {}  # Lưu lại để dùng cho chức năng lọc

    for n in nhoms:
        ma = n.getElementsByTagName("ma")[0].firstChild.data
        ten = n.getElementsByTagName("ten")[0].firstChild.data
        ds_nhom[ma] = ten
        print(f"Mã: {ma}  -  Tên: {ten}")

    print()
    return ds_nhom


# =======================
# 2. Đọc toàn bộ thiết bị
# =======================
def doc_thiet_bi(file_xml):
    print("=== DANH SÁCH THIẾT BỊ ===")
    doc = minidom.parse(file_xml)
    tb_list = doc.getElementsByTagName("thietbi")

    result = []

    for t in tb_list:
        manhom = t.getAttribute("manhom")
        ma = t.getElementsByTagName("ma")[0].firstChild.data
        ten = t.getElementsByTagName("ten")[0].firstChild.data
        result.append((ma, ten, manhom))
        print(f"Mã TB: {ma} | Tên: {ten} | Mã nhóm: {manhom}")

    print()
    return result


# =======================
# 3. Lọc thiết bị theo nhóm
# =======================
def loc_theo_nhom(ds_tb, ma_nhom, ds_nhom):
    print(f"=== THIẾT BỊ THUỘC NHÓM {ma_nhom} - {ds_nhom.get(ma_nhom, '')} ===")

    for tb in ds_tb:
        if tb[2] == ma_nhom:
            print(f"Mã TB: {tb[0]} | Tên: {tb[1]}")

    print()


# =======================
# 4. Xuất nhóm có số thiết bị nhiều nhất
# =======================
def nhom_nhieu_thiet_bi(ds_tb, ds_nhom):
    dem = {}

    for tb in ds_tb:
        nhom = tb[2]
        dem[nhom] = dem.get(nhom, 0) + 1

    # Tìm nhóm có số TB nhiều nhất
    nhom_max = max(dem, key=dem.get)
    so_luong = dem[nhom_max]

    print("=== NHÓM CÓ SỐ THIẾT BỊ NHIỀU NHẤT ===")
    print(f"Mã nhóm: {nhom_max} - Tên: {ds_nhom[nhom_max]} - Số thiết bị: {so_luong}")


# =======================
# CHƯƠNG TRÌNH CHÍNH
# =======================

nhom_file = "nhomthietbi.xml"
thietbi_file = "ThietBi.xml"

# 1. Đọc nhóm thiết bị
ds_nhom = doc_nhom(nhom_file)

# 2. Đọc thiết bị
ds_tb = doc_thiet_bi(thietbi_file)

# 3. Lọc theo nhóm (ví dụ nhóm n1)
loc_theo_nhom(ds_tb, "n1", ds_nhom)

# 4. Nhóm nhiều thiết bị nhất
nhom_nhieu_thiet_bi(ds_tb, ds_nhom)
