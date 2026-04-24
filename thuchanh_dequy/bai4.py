def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
print("ƯCLN =", gcd(a, b))