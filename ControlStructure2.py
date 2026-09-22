#---soal 2---
Mh1= float(input("Masukkan nilai pertama:"))
Mh2= float(input("Masukkan nilai kedua:"))
Mh3= float(input("Masukkan nilai ketiga:"))

if Mh1 >=Mh2 and Mh1 >=Mh3:
    terbesar = Mh1
elif Mh2 >=Mh1 and Mh2 >=Mh3:
    terbesar = Mh2
else:
    terbesar = Mh3
print("Nilai terbesar:", terbesar)