#Câu 10: Xử lý Ma Trận
'''
Yêu cầu:
Nhập 2 matrix A, B.
Cộng 2 matrix
Viết hàm tính matrix hoán vị➔áp dụng để tìm cho A, B
'''

# Hàm nhập ma trận
def nhap_matrix(ten):
    m = int(input(f"Nhập số dòng của ma trận {ten}: "))
    n = int(input(f"Nhập số cột của ma trận {ten}: "))
    print(f"Nhập các phần tử cho ma trận {ten}:")
    matrix = []
    for i in range(m):
        hang = []
        for j in range(n):
            x = float(input(f"{ten}[{i}][{j}] = "))
            hang.append(x)
        matrix.append(hang)
    return matrix

# Hàm in ma trận
def xuat_matrix(matrix):
    for hang in matrix:
        print(hang)

# Hàm cộng hai ma trận
def cong_matrix(A, B):
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        print("Hai ma trận không cùng kích thước, không thể cộng!")
        return None
    m, n = len(A), len(A[0])
    C = []
    for i in range(m):
        hang = []
        for j in range(n):
            hang.append(A[i][j] + B[i][j])
        C.append(hang)
    return C

# Hàm hoán vị ma trận
def hoanvi_matrix(A):
    m, n = len(A), len(A[0])
    HT = []
    for j in range(n):
        hang = []
        for i in range(m):
            hang.append(A[i][j])
        HT.append(hang)
    return HT

#  Main 
print("NHẬP MA TRẬN A")
A = nhap_matrix("A")

print("NHẬP MA TRẬN B")
B = nhap_matrix("B")

print("\nMa trận A:")
xuat_matrix(A)
print("\nMa trận B:")
xuat_matrix(B)

C = cong_matrix(A, B)
if C:
    print("\nTổng ma trận A + B:")
    xuat_matrix(C)

print("\nHoán vị ma trận A:")
xuat_matrix(hoanvi_matrix(A))

print("\nHoán vị ma trận B:")
xuat_matrix(hoanvi_matrix(B))

