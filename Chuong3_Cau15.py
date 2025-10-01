#Câu 15: Giải thích cách chạy các dòng lệnh range
'''
Yêu cầu:
(a) range(5)
(b) range(5, 10)
(c) range(5, 20, 3)
(d) range(20, 5, -1)
(e) range(20, 5, -3)
(f) range(10, 5)
(g) range(0)
(h) range(10, 101, 10)
(i) range(10, -1, -1)
(j) range(-3, 4)
(k) range(0, 10, 1)
'''
'''
Trả lời.
range(start, stop, step)
start: giá trị bắt đầu (nếu bỏ qua thì mặc định = 0).
stop: giá trị dừng (không bao gồm stop).
step: bước nhảy (nếu bỏ qua thì mặc định = 1).

(a) range(5)
Tương đương range(0, 5, 1) → kết quả: [0, 1, 2, 3, 4].
(b) range(5, 10)
Bắt đầu từ 5, nhỏ hơn 10, bước 1 → [5, 6, 7, 8, 9].
(c) range(5, 20, 3)
Bắt đầu từ 5, nhỏ hơn 20, bước 3 → [5, 8, 11, 14, 17].
(d) range(20, 5, -1)
Bắt đầu từ 20, lớn hơn 5, bước -1 → [20, 19, 18, ..., 6].
(e) range(20, 5, -3)
Bắt đầu từ 20, giảm dần đến >5, bước -3 → [20, 17, 14, 11, 8].
(f) range(10, 5)
Mặc định bước là +1. Nhưng 10 > 5, nên không thỏa điều kiện → rỗng [].
(g) range(0)
Mặc định là range(0, 0, 1) → rỗng [].
(h) range(10, 101, 10)
Bắt đầu từ 10, đến 100, bước 10 → [10, 20, 30, ..., 100].
(i) range(10, -1, -1)
Bắt đầu từ 10, dừng trước -1, bước -1 → [10, 9, 8, ..., 1, 0].
(j) range(-3, 4)
Bắt đầu từ -3, đến 3 (nhỏ hơn 4), bước 1 → [-3, -2, -1, 0, 1, 2, 3].
(k) range(0, 10, 1)
Bắt đầu từ 0, nhỏ hơn 10, bước 1 → [0, 1, 2, 3, 4, 5, 6, 7, 8, 9].
'''