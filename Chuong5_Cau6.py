#Câu 6: Trích lọc số âm trong chuỗi
'''
Yêu cầu:
Viết một hàm đặt tên là NegativeNumberInStrings(str). Hàm này có đối số truyền vào
là một chuỗi bất kỳ, Hãy viết lệnh để xuất ra các số nguyên âm trong chuỗi.
Ví dụ: Nếu nhập vào chuỗi “abc-5xyz-12k9l--p” thì hàm phải xuất ra được 2 số nguyên
âm đó là -5 và -12
'''
def NegativeNumberInStrings(s):
    nums = []       # Danh sách chứa các số âm tìm được
    temp = ""       # Dùng để lưu tạm giá trị số âm khi quét

    i = 0
    while i < len(s):
        # Nếu gặp dấu '-' và ký tự sau nó là chữ số thì bắt đầu lấy số âm
        if s[i] == '-' and i + 1 < len(s) and s[i + 1].isdigit():
            temp = '-'  # bắt đầu ghi nhận dấu âm
            i += 1
            # Lấy toàn bộ chữ số sau dấu '-'
            while i < len(s) and s[i].isdigit():
                temp += s[i]
                i += 1
            # Thêm số âm tìm được vào danh sách
            nums.append(int(temp))
        else:
            i += 1

    # Xuất kết quả
    if nums:
        print("Các số nguyên âm trong chuỗi là:", *nums)
    else:
        print("Không có số nguyên âm nào trong chuỗi.")

# --- Chạy thử ---
s = input("Nhập vào một chuỗi: ")
NegativeNumberInStrings(s)
