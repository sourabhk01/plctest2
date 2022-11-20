import pratlang

while True:
		text = input('pratlang ')
		result, error = basic.start(text)

		if error: print(error.as_string())
		else: print(result)
