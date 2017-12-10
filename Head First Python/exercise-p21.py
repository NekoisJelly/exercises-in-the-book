# coding:utf-8


movies = ["The Holy Grail", 1975, "Terry Jones & Terry Gilliam", 91, ["Graham Chapman", ["Micheal Palin", "John Cleese", "Terry Gilliam", "Eric Idle", "Terry Jones"]]]

for i in movies:
	if isinstance(i, list):
		for ii in i:
			if isinstance(ii, list):
				for iii in ii:
					print(iii)
			else:
				print(ii)
	else:
		print(i)