again = "Да"
while again == 'Да':
    grp = 1799
    grh = 1854
    grl = 1814
    gre = 1895
    grg = 1934
    tra = 0
    fla = 5
    age_Pushkin = float(input('введите год рождения Пушкина: '))
    age_Holms = float(input('введите год рождения Шерлока Холмса: '))
    age_Lermontov = float(input('введите год рождения Лермонтова: '))
    age_Esenin = float(input('введите год рождения Есенина: '))
    age_Gagarin = float(input('введите год рождения Гагарина: '))
    If  age_Pushkin == grp:
         tra = tra + 1
    If  age_Holms == grh:
         tra = tra + 1
    If  age_Lermontov == grl:
         tra = tra + 1
    If  age_Esenin == gre:
         tra = tra + 1
    If  age_Gagarin == grg:
         tra = tra + 1
    fla = 5 - tra
    ptra = tra / 5 * 100
    pfla = fla / 5 * 100
    Print ("правильных ответов :" , tra , ptra)
    Print ("Не правильных ответов ;" , fla , pfla)
    again = (input('Попробовать еще раз? '))

print("Всего хорошего")
print('end')