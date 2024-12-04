#!/usr/bin/env python
# -*- coding: utf-8 -*-



def order(values: list = None) -> list:
    list_values = []
    while len(list_values) != 10:
        # TODO: demander les valeurs ici
        value = input('Entrez une valeur: ')
        list_values.append(value)

    print(sorted(list_values))
    return sorted(list_values)


def anagrams(words: list = None) -> bool:
    list_mots = []

    if words is None:
        # TODO: demander les mots ici
        pm = input('Entrez un mot: ')
        list_mots.append(pm)
        dm = input('Entrez un deuxième mot: ')
        list_mots.append(dm)

    val = False
    if sorted(list_mots[0]) == sorted(list_mots[1]):
        val = True
    print(val)
    return val


def contains_doubles(items: list) -> bool:
    for i in items:
        if items.count(i) > 1:
            return True


    return False


def best_grades(student_grades: dict) -> dict:
    top_student = ''
    top_student_grade = 0

    for key, value in student_grades.items():
        moyenne = sum(value) / len(value)
        if moyenne > top_student_grade:
            top_student = key
            top_student_grade = moyenne



    # TODO: Retourner un dictionnaire contenant le nom de l'étudiant ayant la meilleure moyenne ainsi que sa moyenne
    return {top_student: top_student_grade}


def frequence(sentence: str) -> dict:
    # TODO: Afficher les lettres les plus fréquentes
    #       Retourner le tableau de lettres
    words = sentence.split()
    frequency = {}
    for word in words:
        for letter in word:
            if letter in frequency:
                frequency[letter] += 1
            else:
                frequency[letter] = 1

    sorted_frequency = dict(sorted(frequency.items(), key=lambda item: item[1], reverse=True))
    for i in sorted_frequency:
        if sorted_frequency[i] > 5:
            print(f"Le caractère {i} revient {sorted_frequency[i]} fois.")


    return sorted_frequency


def get_recipes():
    # TODO: Demander le nom d'une recette, puis ses ingredients et enregistrer dans une structure de données
    name = input("Quel est le nom de votre recette?\n")
    ingredient = input("Entrer la liste d'ingrédients? Séparer les ingrédiants par une ,\n").split(",")

    return {name: ingredient}




def print_recipe(ingredients) -> None:
    # TODO: Demander le nom d'une recette, puis l'afficher si elle existe
    name = input("Quel est le nom de votre recette?\n")

    if name in ingredients:
        print(ingredients[name])
    else:
        print("Cette recette n'est pas dans le livre!")
        print_recipe(ingredients)




def main() -> None:
    print(f"On essaie d'ordonner les valeurs...")
    order()

    print(f"On vérifie les anagrammes...")
    anagrams()

    my_list = [3, 3, 5, 6, 1, 1]
    print(f"Ma liste contient-elle des doublons? {contains_doubles(my_list)}")

    grades = {"Bob": [90, 65, 20], "Alice": [85, 75, 83]}
    best_student = best_grades(grades)
    print(f"{list(best_student.keys())[0]} a la meilleure moyenne: {list(best_student.values())[0]}")

    sentence = "bonjour, je suis une phrase. je suis compose de beaucoup de lettre. oui oui"
    frequence(sentence)

    print("On enregistre les recettes...")
    recipes = get_recipes()

    print("On affiche une recette au choix...")
    print_recipe(recipes)


if __name__ == '__main__':
    main()
