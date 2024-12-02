#!/usr/bin/env python
# -*- coding: utf-8 -*-
from attr.validators import max_len


def get_num_letters(text):
    count = 0
    for l in text:
        if l.isalnum():
            count += 1
    return count


def get_word_length_histogram(text):
    words = text.split()
    max_length = max(get_num_letters(word) for word in words)
    histogram = [0] * (max_length + 1)

    for word in words:
        letter_count = get_num_letters(word)
        histogram[letter_count] += 1

    return histogram


def format_histogram(histogram):
    ROW_CHAR = "*"
    alignment = len(str(len(histogram) - 1))
    return "\n".join([f"{i : >{alignment}} {ROW_CHAR * elem}" for i, elem in enumerate(histogram) if i != 0])


def format_horizontal_histogram(histogram):
    BLOCK_CHAR = "|"
    LINE_CHAR = "¯"
    max_height = max(histogram)
    result = ""
    for i in range(max_height - 1, -1, -1):

        result += "".join([BLOCK_CHAR if elem >= i + 1 else " " for elem in histogram[1:]]) + "\n"

    result += LINE_CHAR * len(histogram)
    return result



if __name__ == "__main__":
    word = "est?"
    print(f"The number of characters for '{word}' is: {get_num_letters(word)}")
    spam = "Stop right there criminal scum! shouted the guard confidently."
    eggs = get_word_length_histogram(spam)
    print(eggs, "\n")
    print(format_histogram(eggs), "\n")
    print(format_horizontal_histogram(eggs))
