#Author: Alfa Khoirin
#NIM: 120450015
#Affiliation : Sains Data Itera
#Date : 4 March 2022
#Program Description : Program to solve simple encryption password problem

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