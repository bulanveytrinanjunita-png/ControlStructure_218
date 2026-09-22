#---soal 1---
percentage = float(input("Masukkan nilai persentase mahasiswa:"))
if percentage >= 90:
    print("Luar Biasa")
elif percentage >= 80:
    print("Sangat baik")
elif percentage >= 70:
    print("Baik")
elif percentage >= 60:
    print("Cukup")
else:
    print("Kurang")
