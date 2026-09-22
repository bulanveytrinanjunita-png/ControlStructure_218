nilai_Mh = int(input("Masukkan nilai n (jumlah suku fibonacci)"))

Mh1, Mh2 = 0,1
hitung = 0

print("Deret Fibonacci:")
if nilai_Mh <= 0:
    print("Silahkan masukkan bilangan bulat positif lebih dari 0.")
elif nilai_Mh == 1:
    print(Mh1)
else:
    while hitung < nilai_Mh:
        print(Mh1, end=" ")

        Mh3 = Mh1 + Mh2
        Mh1 = Mh2
        Mh2 = Mh3
        hitung += 1