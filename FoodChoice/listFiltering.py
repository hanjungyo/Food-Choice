def veganistfiltering(key):
    if key == "Vegan":
        dbfilename = 'vegan_meal.txt'

        fH = open(dbfilename, 'r')
        line = fH.read()
        fH.close()
        vegan_meal = eval(line)
        return  vegan_meal
    elif key == "Non_Vegan":
        dbfilename = 'non_vegan_meal.txt'

        fH = open(dbfilename, 'r')
        line = fH.read()
        fH.close()
        non_vegan_meal = eval(line)
        return  non_vegan_meal

def al_listfiltering(i, key, list):
    if key == '없음':
        for meal in i:
            list.append(meal)
    else:
        for meal in i:
            meal_contain = i[meal]
            if meal_contain['알레르기'] != key:
                list.append(meal)


def people_listfiltering(i, key, vegan_list, list):
    if i in vegan_list:
        meal_people = vegan_list[i]
        if meal_people['인용'] != key:
            list.remove(i)

def kind_listfiltering(i, key, vegan_list, list):
    if i in vegan_list:
        meal_kind = vegan_list[i]
        if meal_kind['종류'] != key:
            list.remove(i)





if __name__ == '__main__':
    meal_list = []
    al_listfiltering(veganistfiltering("Vegan"), '우유', meal_list)
    for i in meal_list[:]:
        people_listfiltering(i, '1인용', veganistfiltering("Vegan"), meal_list)
    print(meal_list)
    for i in meal_list[:]:
        kind_listfiltering(i, '중식', veganistfiltering("Vegan"), meal_list)
    print(meal_list)