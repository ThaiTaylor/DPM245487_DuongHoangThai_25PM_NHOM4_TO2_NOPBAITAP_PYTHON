#Câu 18: Vẽ các hình dưới đây
'''
Yêu cầu:
Với n là chiều cao của hình, hãy dựa vào n để Vẽ các hình dưới đây

Hình 1:
n = int(input("Nhập n: "))
for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or j == 0 or j == n-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

Hình 2:
n = int(input("Nhập n: "))
for i in range(1, n+1):
    for j in range(i):
        print("*", end=" ")
    print()

Hình 3:
n = int(input("Nhập n: "))

for i in range(n):
    for j in range(n):
        if j == 0 or j == i or i == n-1:   # cạnh trái, cạnh chéo, cạnh đáy
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

'''
