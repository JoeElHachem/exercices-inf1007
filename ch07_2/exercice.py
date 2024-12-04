#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import deque


def get_fibonacci_number(index):

	return (
		0 if index == 0 else
		1 if index == 1 else
		get_fibonacci_number(index - 1) + get_fibonacci_number(index - 2)
	)

def get_fibonacci_sequence(length):
	seq = [0, 1]
	if length <= 2:
		return seq[0:length]
	for i in range(2, length):
		seq.append(seq[-1] + seq[-2])
	return seq



def get_sorted_dict_by_decimals(elems):
	return dict(sorted(elems.items(), key=lambda e: e[1] % 1.0))

def fibonacci_numbers(length):

	init_values = [0, 1]

	for elem in init_values[0:length]:
		yield elem

	last_elems = deque(init_values)
	for i in range(len(init_values), length):

		fibo_number = last_elems[-1] + last_elems[-2]

		last_elems.append(fibo_number)

		last_elems.popleft()
		yield fibo_number

def build_recursive_sequence_generator(initial_values, recursive_def, keep_whole_sequence=False):

	def recursive_generator(length):

		for elem in initial_values[0:length]:
			yield elem

		last_elems = deque(initial_values)

		for i in range(len(initial_values), length):

			current_element = recursive_def(last_elems)

			last_elems.append(current_element)

			if not keep_whole_sequence:
				last_elems.popleft()

			yield current_element

	return recursive_generator



if __name__ == "__main__":
	get_fibonacci_number(4)
	print([get_fibonacci_number(0), get_fibonacci_number(1), get_fibonacci_number(2)])
	print([get_fibonacci_number(i) for i in range(10)])
	print()

	print(get_fibonacci_sequence(1))
	print(get_fibonacci_sequence(2))
	print(get_fibonacci_sequence(10))
	print()

	spam = {
		2: 2.1,
		3: 3.3,
		1: 1.4,
		4: 4.2
	}
	eggs = {
		"foo": 42.6942,
		"bar": 42.9000,
		"qux": 69.4269,
		"yeet": 420.1337
	}
	print(get_sorted_dict_by_decimals(spam))
	print(get_sorted_dict_by_decimals(eggs))
	print()

	for fibo_num in fibonacci_numbers(10):
		print(fibo_num, end=" ")
	print("\n")

	def fibo_def(last_elems):
		return last_elems[-1] + last_elems[-2]
	fibo = build_recursive_sequence_generator([0, 1], fibo_def)
	for fi in fibo(10):
		print(fi, end=" ")
	print("\n")

	# Pour la série de Lucas, la définition récursive est L[i] = L[i-1] + L[i-2], où L[0] = 2, L[1] = 1.
	# C'est la même chose que la série de Fibonacci, mais avec des valeurs initiales différentes
	lucas = build_recursive_sequence_generator([2, 1], lambda seq: seq[-1] + seq[-2])
	print(f"Lucas : {[elem for elem in lucas(10)]}")
	# Pour Perrin, on a P[i] = P[i-2] + P[i-3], avec P[0] = 3, P[1] = 0, P[2] = 2
	perrin = build_recursive_sequence_generator([3, 0, 2], lambda seq: seq[-2] + seq[-3])
	print(f"Perrin : {[elem for elem in perrin(10)]}")
	# Pour Hofstadter-Q, on a Hq[i] = Hq[Hq[i-1]] + Hq[Hq[i-2]], avec P[0] = 1, P[1] = 1
	# Notez que celle-ci utilise les valeurs précédentes commes indice dans la suite pour aller chercher des valeurs, on a donc besoin de garder la séquence au complet en mémoire (on ne sait pas d'avance où vont aller ces indices).
	hofstadter_q = build_recursive_sequence_generator([1, 1], lambda seq: seq[-seq[-1]] + seq[-seq[-2]], True)
	print(f"Hofstadter-Q : {[elem for elem in hofstadter_q(10)]}")
