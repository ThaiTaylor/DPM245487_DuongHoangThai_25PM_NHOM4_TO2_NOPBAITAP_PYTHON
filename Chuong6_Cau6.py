#Câu 6: Nhập vào 1 list có N số ngẫu nhiên KHÔNG TRÙNG NHAU
import random

# Nhập số lượng phần tử
N = int(input("Nhập số lượng phần tử N: "))

# Tạo list ngẫu nhiên KHÔNG TRÙNG trong đoạn [1..100]
lst = random.sample(range(1, 101), N)

print("Danh sách ngẫu nhiên không trùng là:")
print(lst)
