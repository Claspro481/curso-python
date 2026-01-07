#indices 012345
 
#Indiexacion de base cero 

#Podemos tener posiciones en todos lados desde numeros strings y listas o tuplas 

texto = "Lectura "
print(texto[0]) #L
print(texto[1])
print(texto[6])

#EJEMPLOS CON STRING 
#Remplazar texto
curso = "Este curso es de JavasCript, Javascript"
print(curso.replace("JavasCript", "Python"))
texto_dividido = texto.replace
#Acceder a un caracter especifico 
print(curso[5])
print(curso[-1]) #desde el final indice negativo 


#Ejemplo con listas 
numeros = [10, 20, 30, 40,  50]
#indice    0   1   2   3     4
print(numeros[0])
print(numeros[2])

#Ejemplos con tuplas 
tupla = ("Python", "JavaScript", "C++")
print(tupla[0])

#Slicing Podemos obtener subcadenas o sublistas 
text = "Motorcycle"
print(text[0:4])
print(text[:3]) 
print(text[2:])

palabra = "Pythonista"
print(palabra[0:6])
