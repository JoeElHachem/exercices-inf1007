#!/usr/bin/env python
# -*- coding: utf-8 -*-
from itertools import count

from fontTools.misc.cython import returns


def is_even_len(string: str) -> bool:
    return True if len(string) % 2 == 0 else False


def remove_third_char(string: str) -> str:
    new_string = string[:2] + string[3:]
    return new_string


def replace_char(string: str, old_char: str, new_char: str) -> str:
    return string.replace(old_char,new_char)


def get_number_of_char(string: str, char: str) -> int:
    count = 0
    for c in string :
        if c in char:
            count += 1

    return count


def get_number_of_words(sentence: str, word: str) -> int:
    return sentence.count(word)



def main() -> None:
    chaine = "Bonjour!"
    if is_even_len(chaine):
        print(f"Le nombre de caractère dans la chaine {chaine} est pair")
    else:
        print(f"Le nombre de caractère dans la chaine {chaine} est impair")

    chaine = "salut monde!"
    print(f"On supprime le 3e caratère dans la chaine: {chaine}. Résultat : {remove_third_char(chaine)}")

    chaine = "hello world!"
    print(f"On remplace le caratère w par le caractère z dans la chaine: {chaine}. Résultat : {replace_char(chaine, 'w', 'z')}")

    print(f"Le nombre d'occurrence de l dans {chaine} est : {get_number_of_char(chaine, 'l')}")
    
    chaine = "Baby shark doo doo doo doo doo doo"
    print(f"L'occurence du mot doo dans la chaine {chaine} est: {get_number_of_words(chaine, 'doo')}")


if __name__ == '__main__':
    main()
