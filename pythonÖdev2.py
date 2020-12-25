not100=int(input('Notunuzu Giriniz:'))
not4=float(not100/25)
if(not4<1):
    print("Kaldın...")
elif(1<=not4<=2):
    print("Daha çok çalışmalısın.")
elif(2<=not4<3):
    print("İyi.")
elif(3<=not4<=3.5):
    print("Çok iyi.")
else:
    print("DAHİ!")
