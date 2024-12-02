#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random




def format_bill_total(data):
    INDEX_NAME = 0
    INDEX_QUANTITY = 1
    INDEX_PRICE = 2

    sous_total = 0

    for item in data:
        sous_total += item[INDEX_QUANTITY] * item[INDEX_PRICE]

    taxes = sous_total * 0.15
    total = sous_total + taxes

    return f"Sous-total: {sous_total:.2f} $\nTaxes: {taxes:.2f} $\nTotal: {total:.2f} $"


def format_bill_items(data):
    INDEX_NAME = 0
    INDEX_QUANTITY = 1
    INDEX_PRICE = 2

    result = ""
    for item in data:
        total_item = item[INDEX_QUANTITY] * item[INDEX_PRICE]
        result += f"{item[INDEX_NAME]} {total_item:.2f} $\n"




    return result


def format_number(number, num_decimal_digits):
    return f"{number:.{num_decimal_digits}f}"


def get_triangle(num_rows):


    width = num_rows * 2 + 1
    result = []


    result.append("+" * width)


    for i in range(num_rows):
        spaces = num_rows - i - 1
        a_count = i * 2 + 1
        result.append(f"+{' ' * spaces}{'A' * a_count}{' ' * spaces}+")


    result.append("+" * width)

    return "\n".join(result)


if __name__ == "__main__":
    purchases = [
        ("chaise ergonomique", 1, 399.99),
        ("g-fuel", 69, 35.99),
        ("blue screen", 2, 39.99)
    ]
    print(format_bill_items(purchases).strip())
    print("- - - - - - - - - - - - - - - - - - -")
    print(format_bill_total(purchases).strip())

    print("\n------------------")

    print(format_number(-1420069.0678, 2))

    print("\n------------------")

    print(get_triangle(2))
    print(get_triangle(5))
