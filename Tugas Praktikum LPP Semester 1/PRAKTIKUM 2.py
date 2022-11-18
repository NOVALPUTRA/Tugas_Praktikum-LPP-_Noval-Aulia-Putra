#GAME TEBAK ANGKA
import random
angka_random = random.randint(1, 20)
print ("="*40)
print("Selamat datang di Game Tebak Angka")
print ("="*40)
print("\n")
print ("Kami sudah menentukan angka yang harus ditebak, silahkan masukan angka tebakan anda :")
batas_percobaan = 8
for percobaan in range(batas_percobaan) :
    jawaban = int(input(f'\n[Percobaan ke {percobaan + 1}] Masukkan angka: '))
    if jawaban == angka_random :
        print ("Selamat Kamu benar, Angka rahasianya adalah =", angka_random)
        break
    else :
        if jawaban < angka_random :
            print ("Angka tebakan anda terlalu kecil silahkan coba kembali")
        if jawaban > angka_random :
            print ("Angka tebakan anda terlalu besar silahkan coba kembali")
else : 
    print ("\n")
    print ("Kesempatan anda untuk menebak sudah habis, kamu sudah salah menebak sebanyak " + str(batas_percobaan) + "!!")