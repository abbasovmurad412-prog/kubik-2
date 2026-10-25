
cislo = int(input("Введите двузначное число: "))

pervoe_cislo = cislo // 10
vtoroe_cislo = cislo % 10

novoe_cislo = vtoroe_cislo * 10 + pervoe_cislo

print("Новое число:", novoe_cislo)
