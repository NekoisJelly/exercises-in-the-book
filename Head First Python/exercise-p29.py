# coding: utf-8
import os


def print_lol(the_list, level=0):
	for i in the_list:
		if isinstance(i, list):
			print_lol(i, level+1)
		else:
			for t in range(level):
				print('\t', end='')
			print(i)


movies = ["The Holy Grail", 1975, "Terry Jones & Terry Gilliam", 91,
 ["Graham Chapman", ["Micheal Palin", "John Cleese", "Terry Gilliam",
  "Eric Idle", "Terry Jones"]]]
print_lol(movies)
