#Author: Alfa Khoirin
#NIM: 120450015
#Kelas: Pemrograman berbasis fungsi - RA
#Prodi : Sains Data

#Soal 3a
def enkripsi(pw):
    password = list(pw)
    ascii = list()
    for char in password:
        asciichar = ord(char)
        ascii.append(asciichar)

    enkripsipassword = ""
    for nilai in ascii:
        pertama = nilai//26 + 80
        kedua = nilai%26 + 80
        if pertama > kedua:
            ketiga = '+'
        else:
            ketiga = '-'

        enkripsipassword = enkripsipassword + chr(pertama) + chr(kedua) + ketiga


    return enkripsipassword

def kembalikanpw(pw):
    ascii = list()
    for i in range(0, len(pw), 3):
        password = [pw[i:i+3]]
        for huruf in password:
            pertama = ord(huruf[0]) - 80
            kedua = ord(huruf[1]) - 80
            value = 26 * pertama + kedua
            ascii.append(value)

    passwordasli = ''
    for i in ascii:
        char = chr(i)
        passwordasli = passwordasli + char

    return passwordasli

#soal 3b
pwasli = 'anakanakcerdas2020'
Hasil = enkripsi(pwasli)
print('Enkripsi password anda adalah : ', Hasil)

#Soal 3c
pwenkripsi = 'Sc-TV-Sc-TS+T[-Sc-TQ+TV-T[-Sf-Sc-T\-Sc-Qh-Qf-Qh-Qf-TS+Sg-Se-Sg-'
passasli = kembalikanpw(pwenkripsi)
print('Password asli anda adalah : ', passasli)