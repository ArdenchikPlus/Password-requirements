n=input()
check1=0
check2=False
check3=False
check4=False
result=0
num="123456789"
st="!@#$%"
for i in range(len(n)):
    check1=check1+1
    if n[i].isupper():
        check2=True
    if n[i] in num:
        check3=True
    if n[i] in st:
        check4=True
if check1 < 8:
    print("Ошибка: в пароле меньше 8 символов")
else:
    result=result+1
if check2 != True:
    print("Ошибка: в пароле нет заглавной буквы")
else:
    result=result+1
if check3 == False:
    print("Ошибка: в пароле нет цифр")
else:
    result=result+1
if check4 == False:
    print("Ошибка: в пароле нет символов")
else:
    result=result+1
if result == 4:
    print("Ваш пароль надёжный")
