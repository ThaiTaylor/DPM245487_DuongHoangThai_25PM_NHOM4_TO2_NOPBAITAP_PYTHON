#Câu 7: Viết chương trình nhập vào một dãy các số theo thứ tự tăng, nếu nhập sai quy cách thì yêu cầu nhập lại. In dãy số sau khi đã nhập xong

# Nhập số lượng phần tử
n = int(input("Nhập số lượng phần tử: "))

lst = []

for i in range(n):
    while True:
        x = int(input(f"Nhập phần tử thứ {i + 1}: "))
        # Nếu là phần tử đầu tiên hoặc lớn hơn phần tử trước đó
        if i == 0 or x > lst[-1]:
            lst.append(x)
            break
        else:
            print("Số phải lớn hơn số trước đó! Nhập lại.")

print("Dãy số tăng dần vừa nhập là:")
print(lst)
