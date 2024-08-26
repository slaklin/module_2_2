first = input("Введите первое число: ")
second = input("Введите второе число: ")
third = input("Введите третье число: ")
if first == second == third:
    print(3)
elif first == second or second == third or first == third:
    print(2)
elif not first == second or not second == third or not first == third:
    print("0 - Введенные вами числа не равны друг другу")