again = "Да"
while again == 'Да':
    age_Pushkin =int(input('введите год рождения Пушкина: '))
    age_Holms = float(input('введите год рождения Шерлока Холмса: '))
    age_Lermontov = float(input('введите год рождения Лермонтова: '))
    age_Esenin = float(input('введите год рождения Есенина: '))
    age_Gagarin = float(input('введите год рождения Гагарина: '))
    grp = 1799
    grh: float = 1854
    grl: float = 1814
    gre: float = 1895
    grg: float = 1934
    fla: float = 0
    tra = 0
    if  age_Pushkin != grp:
         fla = fla + 1
    elif age_Holms !=  grh:
         fla = fla + 1
    elif age_Lermontov !=  grl:
         fla = fla + 1
    elif age_Esenin !=  gre:
         fla = fla + 1
    elif age_Gagarin != grg:
         fla = fla + 1
    else: tra = 5 - fla
    ptra = tra / 5 * 100
    pfla = fla / 5 * 100
    print ("правильных ответов :" , tra, ptra)
    print ("Не правильных ответов ;" , fla, pfla)
    again = (input('Попробовать еще раз? '))
print("Всего хорошего")
print('end')
