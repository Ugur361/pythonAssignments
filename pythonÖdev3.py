hesapno=13579
sifre=4545
limit=500
hesapbakiye=250
musterino=int(input("Hesap numaranızı giriniz:"))
musterisifre=int(input("Şifrenizi giriniz:"))
if(hesapno==musterino and musterisifre==sifre):
   print("Bakiyeniz:{} İşlem limitiniz:{}".format(hesapbakiye,limit))
else:
        print("Hesap numarası veya şifre yanlış!")






