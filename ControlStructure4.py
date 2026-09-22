nilai_Mh = int(input("Masukkan batas nilai persentase mahasiswa:"))

print(f"bilangan ganjil sampai dengan {nilai_Mh}:")

for i in range(1, nilai_Mh + 1, 2):
    print(i, end=" ")
print()
