# Entero a cadena
num = 19
num_str = str(num)
print(num_str)  # "19"

# Cadena a entero
num_str = "30"
num = int(num_str)
print(num)  # 30

# Decimal a cadena
decimal = 4.50
decimal_str = str(decimal)
print(decimal_str)  # "4.50"

# Cadena a decimal
decimal_str = "3.719"
decimal = float(decimal_str)
print(decimal)  # 3.719

multilinea = """Esta cadena es de múltiples líneas en Python."""
print(multilinea)

cadena = "Hola, Luis Fernando"
print(len(cadena))

cadena = "Hola, Luis Fernando"
n = 7
print(cadena[:n])

cadena = "Hola, Luis"
inicio = 7
fin = 14
print(cadena[inicio:fin])

cadena = "Hola, Fernando"
n = 7
print(cadena[-n:])

cadena = "Hola, Luis"
print(cadena.upper())

cadena = "Hola, Luis Fernando"
print(cadena.lower())

multilinea = """Esta es otra cadena de líneas multiples en Python."""
print(multilinea)

cadena = "   Hola, Fernando   "
print(cadena.strip())

cadena = "Hola, Luis"
print(cadena.replace("Luis Fernando", "Python"))

cadena = "Hola, Luis Fernando"
print(cadena.replace("Luis Fernando", "Python"))

nombre = "Luis Fernando Jimenez"
edad = 19
print(f"Me llamo {nombre} y tengo {edad}años.")






