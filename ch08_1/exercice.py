#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO: Importez vos modules ici
import os
import json


# TODO: Définissez vos fonction ici
def compare_files(fpath, cpath):
    with open(fpath, "r") as f1, open(cpath, "r") as f2:
        for i, (line1, line2) in enumerate(zip(f1, f2), start=1):
            if line1 != line2:
                print(f"The files are not identical. Line {i + 1} is different.")
                print(line1)
                print("Is not the same as:")
                print(line2)
                return

    print("The files are identical.")


def replace_space(fpath, cpath):
    with open(fpath, "r") as f1, open(cpath, "w") as f2:
        f2.write(f1.read().replace(" ", "   "))


def grade_notes(npath, tpath, rpath):
    with open(npath, 'r', encoding='utf-8') as note_file:
        notes = note_file.readlines()

    with open(tpath, 'r', encoding='utf-8') as thresholds_file:
        thresholds = json.load(thresholds_file)

    with open(rpath, 'w', encoding='utf-8') as result_file:
        for note in notes:
            note = note.strip()
            for grade, (min_threshold, max_threshold) in thresholds.items():
                if min_threshold <= int(note) < max_threshold:
                    result_file.write(f"{note} {grade}\n")
                    break


def extract_and_sort_numbers(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    numbers = [float(word) for word in content.split() if word.isdigit()]
    return sorted(numbers)

def copy_every_other_line(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
        for index, line in enumerate(infile):
            if index % 2 == 0:
                outfile.write(line)


if __name__ == '__main__':
    if not os.path.exists("output"):
        os.mkdir("output")

    # TODO: Appelez vos fonctions ici, mettez vos fichiers de sortie dans le dossier "output".
