#Câu 5: Viết hàm đệ qui Fibonacci
'''
Yêu cầu:
Dãy Số Fibonacci là dãy số có dạng:
1→1→2→3→5→8→13→21→34→55→89…
Được định nghĩa theo công thức đệ qui như dưới đây:
Nếu N=1,N=2➔FN=1
N>2 FN=FN-1+FN-2
Hãy viết 2 hàm:
- Hàm trả về số Fib tại vị trí thứ N bất kỳ
- Hàm trả về danh sách dãy số Fib từ 1 tới N

'''

# Hàm đệ quy tính số Fibonacci tại vị trí N
def fib(n):
    if n == 1 or n == 2:
        return 1
    return fib(n - 1) + fib(n - 2)

# Hàm trả về danh sách dãy Fibonacci từ 1 tới N
def fib_list(n):
    return [fib(i) for i in range(1, n + 1)]

# Chương trình chính
N = int(input("Nhập N: "))

print(f"Số Fibonacci tại vị trí {N} là:", fib(N))
print(f"Dãy Fibonacci từ 1 tới {N} là:", fib_list(N))
