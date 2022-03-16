with open('Bilangan 1.txt','r') as x:
    bacaisifile1 = x.read()
    ConvertString1 = int(bacaisifile1) #mengubah menjadi interger karena file awal akan terbaca sebagai string
    #Cek Import Data
    print('Nilai Bilangan 1 adalah : ', ConvertString1)

with open('Bilangan 2.txt','r') as y:
    bacaisifile2 = y.read()
    ConvertString2 = int(bacaisifile2) #mengubah menjadi interger karena file awal akan terbaca sebagai string
    #Cek Import Data
    print('Nilai Bilangan 2 adalah : ', ConvertString2)

def Jumlah():
    return ConvertString1 + ConvertString2

print('Hasil dari penjumlahan 100 digit bilangan adalah : ',Jumlah())

