print ("Anda berjalan ke suatu ruangan dan ada 2 pintu yaitu pintu 1 dan pintu 2.")
pintu=input("pintu manakah yang anda pilih: ")
if pintu==1:
    print ("Selamat datang di pintu 1, silakan pilih 3 hal di bawah ini")
    print ("1. Harta")
    print ("2. Tahta")
    print ("3. Wanita")
    pilihan=input("pilihan anda: ")
    if pilihan==1:
	print "Anda Kaya"
    elif pilihan==2:
	print "Anda Raja"
    elif pilihan==3:
	print "Anda Menderita"
elif pintu==2:
    print ("Selamat datang di pintu 2")
    print ("1. Homo")
    print ("2. Tahta")
    pilihan=input("pilihan anda: ")
    if pilihan==1:
	print "anda dimakan"
    elif pilihan==2:
	print "anda ikutan"

print "selesai"
