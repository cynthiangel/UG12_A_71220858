nama = str(input("Masukkan nama :"))
a = 0
for i in range (len(nama)):
    a +=1
    print (nama[:a])

for i in range (len(nama)):
    a -=1
    print(nama[:a])
