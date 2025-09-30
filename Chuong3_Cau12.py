#Câu 12: Xuất Bảng cửu chương 2-->9.
for i in range(1, 11):  # vòng lặp hàng (1 → 10)
    for j in range(2, 10):  # vòng lặp cột (2 → 9)
        print(f"{j} * {i} = {j*i:<2}", end="\t")  # in từng phép tính
    print()  # xuống dòng sau mỗi hàng
