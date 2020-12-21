def clean_character(letra):
		if letra.isalpha():
			return letra.upper()
		return ''


print('Welcome to the palindrome test')
print('press q if you wanna quit')

selection = 'c'
while selection != 'q':
	resultado = ''
	palabra = input('Enter the word you wanna analize: ')
	for i in range(len(palabra)):
		resultado += clean_character(palabra[len(palabra) - 1 - i])
	palabra = palabra.upper()
	print(resultado, palabra)
	if resultado == palabra.upper:
		print(palabra + ' is a palindrome')
	else:
		print(palabra + ' is not a palindrome')
	selection = input('Press q if wanna quit: ')
