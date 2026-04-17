n = int(input("Nhập số n: "))

# Bài 4
chan = 0
le = 0
temp = n

while temp > 0:
    digit = temp % 10
    
    if digit % 2 == 0:
        chan += 1
    else:
        le += 1
        
    temp = temp // 10

print("Số chẵn:", chan)
print("Số lẻ:", le)

# Bài 5
tong = 0
tich = 1
temp = n

while temp > 0:
    digit = temp % 10
    
    tong += digit
    tich *= digit
    
    temp = temp // 10

print("Tổng:", tong)
print("Tích:", tich)

# Bài 6
temp = n
max_digit = 0

while temp > 0:
    digit = temp % 10
    
    if digit > max_digit:
        max_digit = digit
        
    temp = temp // 10

print("Số lớn nhất:", max_digit)

# Bài 7
temp = n
mayman = True

while temp > 0:
    digit = temp % 10
    
    if digit != 6 and digit != 8:
        mayman = False
        break
        
    temp = temp // 10

if mayman:
    print("Là số may mắn")
else:
    print("Không phải số may mắn")