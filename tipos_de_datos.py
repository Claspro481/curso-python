print("--------TIPOS PRIMITIVOS----------")

print("---------STR-----------------")
texto = "Cadena de texto"
print(f"String: {texto}")
texto1 = 'este es un texto'
texto2 = "este es un texto"
texto3 = '''este es un texto'''
texto4 = """este es un texto"""
print(texto1)
print(texto2)
print(texto3)
print(texto4)

print("---------NUMEROS ENTEROS-----------------")
entero = 42
print(f"Entero: {entero}")
entero_grande = 99999999999999
print(f"Entero grande: {entero_grande}")

print("-----------NUMEROS FLOTANTES----------------")
precio = 19.99
print(f"Float: (precio) {precio}")
pi = 3.14159
print(f"Float (pi): {pi}")

print("---------NUMEROS COMPLEJOS-----------------")
numero_complejo = 3 + 3j
print(f"Complex (complejo): {numero_complejo}")
print("Complex (real):", {numero_complejo.real})
print("Complex (imaginario):" , {numero_complejo.imag})


print("---------BOOLEANOS-----------------")
activo = True
verificado = False
print(type(activo), activo)
print(10 > 5) # true
print(10 < 5) # false


print("---------TIPO NONE-----------------")
resultado = None 
print(type(resultado), resultado)


#Tipos de datos 

#Strings 
word = "Hola"
print(word)
#Entero
cantidad = 10
print(cantidad)
#Double
precio = 21.99
print(precio)
#Bool
esVerde = True
print(esVerde)
esRojo = False
print(esRojo)

