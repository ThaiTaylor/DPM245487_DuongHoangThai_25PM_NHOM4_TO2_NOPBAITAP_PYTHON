##Câu 6: Nhập một số n có tối đa 2 chữ số. Hãy cho biết cách đọc ra dạng chữ.
#(vd: n=35 => Ba mươi lăm, n=5 => năm). 

def doc_so(n):
    don_vi = ["", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]

    if n < 10:
        if n == 0:
            return "không"
        return don_vi[n]

    elif n < 20:
        if n == 10:
            return "mười"
        elif n == 15:
            return "mười lăm"
        else:
            return "mười " + don_vi[n % 10]

    else:  # từ 20 đến 99
        chuc = n // 10
        dv = n % 10

        chuoi = don_vi[chuc] + " mươi"

        if dv == 0:
            return chuoi
        elif dv == 1:
            return chuoi + " mốt"
        elif dv == 5:
            return chuoi + " lăm"
        else:
            return chuoi + " " + don_vi[dv]

# --- Chương trình chính ---
n = int(input("Nhập số (0-99): "))
if 0 <= n <= 99:
    print(f"{n} -> {doc_so(n)}")
else:
    print("Vui lòng nhập số trong khoảng 0 đến 99.")
