
#contamos las palabras con len
palabra = "Muercielago"
print(len(palabra))

#Verificamos si existe cierta palabra en un string 
texto1 = "Este curso es de Fundamentos de Python"
estaIncluida = "Python" in texto1
noEstaIncluida = "Java" not in texto1
print(noEstaIncluida)


#Tranformacion de texto 
oracion = "Un barco choco con el hielo"
mayuscula = oracion.upper()
minuscula = oracion.lower()
print(f"Mayusculas : {mayuscula}")
print(f"Minusculas : {minuscula}")

#Limpieza de espacios 
password = "   Password123   "
sin_espacios = password.strip()
print(password)
print(sin_espacios)

#Upper convierte todo a mayusculas 
#Lower todo a minusculas 
#strip deja sin espacios al principio y al final 
'''Strip util para entradas de contrase;as 
con espacios al principio y al final ff'''