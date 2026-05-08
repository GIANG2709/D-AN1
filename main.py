# Tạo file gốc
f = open("fileName.txt", "w", encoding="utf-8")

f.write("""Thuyen va bien
Chi co thuyen moi hieu
Bien menh mong nhuong nao
Chi co bien moi biet
Thuyen di dau ve dau
""")

f.close()

# Đọc file gốc
f = open("fileName.txt", "r", encoding="utf-8")
data = f.read()
f.close()

print("Noi dung goc:\n")
print(data)

# Tách các từ
words = data.split()

# Danh sách từ không trùng
unique_words = []

# Vị trí xuất hiện
positions = []

for word in words:
    if word not in unique_words:
        unique_words.append(word)

    positions.append(unique_words.index(word))

# Ghi file nén
f = open("compressed.txt", "w", encoding="utf-8")

f.write("Tu dien:\n")
f.write(str(unique_words))
f.write("\n\nVi tri:\n")
f.write(str(positions))

f.close()

print("\nDa tao file compressed.txt")

# ===== Khôi phục dữ liệu =====

restored_words = []

for pos in positions:
    restored_words.append(unique_words[pos])

restored_text = " ".join(restored_words)

print("\nNoi dung sau khi khoi phuc:\n")
print(restored_text)