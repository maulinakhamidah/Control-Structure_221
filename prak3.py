n = int(input("Masukkan nilai n untuk batas deret fibonacci:"))

a, n = 0, 1

print("Deret fibonacci hingga", n,":")
while a <= n:
    print(a, end= " ")
    a, b = b, a + b