print('Как тебя зовут? ', end='')
name = input()
print(f'Привет {name}! Я твой лечащий врач.  \
Сколько тебе лет? ', end='')
age = float(input())
if age > 0 and age < 13:
    print("Оооо, какой большой!")
if age > 13 and age < 25:
    print("Мммм, наверное уже целовался?")
if age > 25 and age < 40:
    print("Нуууу уже в самом расцвете сил... \nи возможно без волос.")
if age > 40 and age < 60:
    print("Наверное и член уже не стоит?")
if age > 60 and age < 100:
    print("Хм! Да как комп смог включить?")
elif age == 0 or age > 100:
    print('Такого не бывает!')
