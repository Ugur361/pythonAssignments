a=int(input('Sayı1:'))
b=int(input('Sayı2:'))
c=int(input('Sayı3:'))

if(a>=b) and (a>=c):
    buyuk=a
elif(b>=a) and (b>=c):
    buyuk=b
else:
    buyuk=c
    if (a <= b) and (a <= c):
        kucuk = a
    elif (b <= a) and (b <= c):
        kucuk = b
    else:
        kucuk = c
print(a, b, "ve", c, "sayıları içinde en küçük olan sayı:", kucuk)
print(a,b, "ve", c , "sayıları içinde en büyük olan sayı:",buyuk)