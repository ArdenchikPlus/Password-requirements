n=input()
check1=0
check2=False
result=0
for i in range(len(n)):
    check1=check1+1
    if n[i].isupper():
        check2=True
if check1 < 8:
    print("Ошибка: в пароле меньше 8 символов")
else:
    result=result+1
if check2 != True:
    print("Ошибка: в пароле нет заглавной буквы")
else:
    result=result+1



