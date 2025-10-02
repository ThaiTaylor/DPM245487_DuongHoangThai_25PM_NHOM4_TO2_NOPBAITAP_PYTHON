#Câu 2: Viết Hàm để chơi Game Đoán Số
'''
Yêu cầu:
Máy ra 1 số trong đoạn [1...100]
Trang 35/84
Người chơi đoán số, chỉ được phép đoán sai 7 lần. Mỗi lần đoán sẽ thông báo số
người chơi đoán nhỏ hơn hay lớn hơn số của mày và hiển thị số lần đoán
Game kết thúc khi: Đoán sai quá 7 lần hoặc đoán trúng trước 7 lần.
Sau khi game kết thúc hỏi người chơi có tiếp tục hay không?

'''

import random

def choi_game():
    so_bi_mat = random.randint(1, 100)
    so_lan_doan = 0
    gioi_han = 7
    
    print("Chào mừng bạn đến với trò chơi đoán số!")
    print("Máy đã chọn 1 số trong đoạn [1..100]. Bạn có 7 lần đoán.")

    while so_lan_doan < gioi_han:
        try:
            doan = int(input(f"Lần {so_lan_doan+1}, nhập số bạn đoán: "))
        except ValueError:
            print("Vui lòng nhập số nguyên.")
            continue

        so_lan_doan += 1

        if doan == so_bi_mat:
            print(f"Chính xác! Bạn đã đoán đúng sau {so_lan_doan} lần.")
            break
        elif doan < so_bi_mat:
            print("Số bạn đoán nhỏ hơn số bí mật.")
        else:
            print("Số bạn đoán lớn hơn số bí mật.")

        print(f"Bạn còn {gioi_han - so_lan_doan} lần đoán.")

    else:
        print(f"Bạn đã thua! Số bí mật là {so_bi_mat}.")

while True:
    choi_game()
    tiep = input("Bạn có muốn chơi tiếp không? (c/k): ").lower()
    if tiep != "c":
        print("Cảm ơn bạn đã chơi!")
        break
