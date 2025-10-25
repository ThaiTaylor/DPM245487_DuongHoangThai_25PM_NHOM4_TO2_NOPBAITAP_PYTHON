#Câu 9: Xử lý mảng
'''
Yêu cầu:
Viết chương trình nhập vào một mảng số tự nhiên. Hãy xuất ra màn hình:
- Dòng 1 : gồm các số lẻ, tổng cộng có bao nhiêu số lẻ.
- Dòng 2 : gồm các số chẵn, tổng cộng có bao nhiêu số chẵn.
- Dòng 3 : gồm các số nguyên tố.
- Dòng 4 : gồm các số không phải là số nguyên tố.
M[] ={3,6,7,8,11,17,2,90,2,5,4,5,8}
➔ 3, 7, 11,17, 5(2) ➔6 số lẻ
'''
# Hàm kiểm tra số nguyên tố
def la_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


# Nhập mảng (có thể thay input() để nhập từ bàn phím)
M = [3, 6, 7, 8, 11, 17, 2, 90, 2, 5, 4, 5, 8]

# Tách số lẻ, chẵn
le = [x for x in M if x % 2 != 0]
chan = [x for x in M if x % 2 == 0]

# Tách số nguyên tố và không nguyên tố
nguyento = [x for x in M if la_so_nguyen_to(x)]
khong_nguyento = [x for x in M if not la_so_nguyen_to(x)]

# Xuất kết quả
print("Dòng 1: Số lẻ:", le, f"→ Tổng cộng {len(le)} số lẻ")
print("Dòng 2: Số chẵn:", chan, f"→ Tổng cộng {len(chan)} số chẵn")
print("Dòng 3: Số nguyên tố:", nguyento)
print("Dòng 4: Số không phải nguyên tố:", khong_nguyento)
