# String

name_string = "Ai-Ling"

last_name_string = "González"

print(name_string + last_name_string)

print(name_string + " " + last_name_string)

print(f'Letras del nombre: {[*name_string]}')

print(f'{len(name_string)}')

print(f'Cuarta letra: {name_string[3]}')

print(f'Primeras 4 letras: {name_string[0:4]}')

print(f'upper(): {name_string.upper()}')
print(f'lower(): {name_string.lower()}')
print(f'partition(): {name_string.partition("-")}')

incorrect_name = name_string.replace("i", "x")

print(f'Replace(i, x): {incorrect_name}')

print(f'split(-): {name_string.split("-")}')
print(f'find(-): {name_string.find("-")}')
print(f'isnumeric(-): {name_string.isnumeric()}')

print(f'{name_string[::-1]}')
