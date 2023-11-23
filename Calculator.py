x=int(input("sayı giriniz :"))
y=input("operatör giriniz :")
z=int(input("sayı giriniz :"))


if y == "+":
    sonuc= x + z
elif y == "-":
    sonuc= x - z
elif y == "*":
    sonuc= x * z
elif y == "/":
    sonuc= x / z

while True:
    if y in ('+', "-", "*", "/"):
        print("<3")

    else:
        print("geçerli bir operatör giriniz!!!!")
        break


    print("sonuç :", sonuc)
    break
