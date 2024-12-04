#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO: Importez vos modules ici
import math
from ch06_1.exercice import order, anagrams, contains_doubles, best_grades, frequence
from turtle import *
import re


# TODO: Définissez vos fonction ici
def volume_mass_elipsoide(a, b, c, masse_volumique):
    volume = 4 / 3 * math.pi * a * b * c
    masse = masse_volumique * volume
    return masse


def lettre_frequent(sentence: str) -> dict:
    dictionnaire = frequence(sentence)
    for k, v in dictionnaire.items():
        if v == max(dictionnaire.values()):
            lettre = {k: v}

    return lettre


def draw_tree():
    def draw_branch(branch_len, pen_size, angle):
        if branch_len > 0 and pen_size > 0:
            pensize(pen_size)
            forward(branch_len)
            right(angle)
            draw_branch(branch_len - 10, pen_size - 1, angle - 5)
            left(angle * 2)
            draw_branch(branch_len - 10, pen_size - 1, angle - 5)
            right(angle)
            backward(branch_len)

    setheading(90)
    color("green")
    draw_branch(70, 7, 35)
    done()


def valide(saisie):
    return bool(re.match("^[atgc]+$", saisie))


def saisie(type: str) -> str:
    while True:
        value = input(f"Entrez une {type} d'ADN valide: ")
        if valide(value):
            return value
        print(f"La {type} n'est pas valide")


def proportion(chain: str, sequence: str) -> float:
    return chain.count(sequence) / len(chain)


if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici

    print(volume_mass_elipsoide(2, 4, 6, 10))
    print(lettre_frequent('bonjour'))
    chain = saisie("chaine")
    sequence = saisie("sequence")

    prop = proportion(chain, sequence)
    print("Il y a {0:.2f} % de {1}.".format(prop * 100, sequence))
    pass
