Number = int(input("Введите номер четверти:"))
if (Number == 1):
    print("X > 0 Y > 0")
if (Number == 2):
    print("X < 0 Y > 0")
if (Number == 3):
    print("X < 0 Y < 0")
if (Number == 4):
    print("X > 0 Y < 0")
else:
    print("Такой четверти не существует")