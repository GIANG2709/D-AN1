def power(a, b):
    if b == 0:
        return 1
    return a * power(a, b - 1)

a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
print("a^b =", power(a, b))