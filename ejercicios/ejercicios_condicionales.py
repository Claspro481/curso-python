'''
Realizar un programa que solicite la carga por teclado de dos numeros 
si el primero es mayor al segundo informar su suma ydiferencia 
en caso contrarioo informar el producto y la division del primeroi
respecto al segundo 
'''
num1=int(input("Ingrese el primer numero: "))
num2=int(input("Ingrese el segundo numero: "))
suma = num1 + num2
producto = num1 * num2
division = num1 / num2

if num1> num2:
    print(f"Suma: {suma}")
else:
    print(f"Porducto: {producto}, division: {division}")

'''Se ingresa por teclado un numero psotivo
de uno o dos digitos '''

numero1=int(input("Ingrese un valor entero de 1 o 2 digitos: "))
if numero1<10:
    print("Tiene un solo digito")
else:
    print("Tiene dos digitos")


'''Desarrolla un programa que solicite el cilindraje de una moto. Si es menor a 125, informa 'Licencia A1'. 
Si está entre 125 y 499 (inclusive), informa 'Licencia A2'. Si es 500 o más, informa 'Licencia A3'.'''

cilindraje = int(input("Que cilindrajes es la motocicleta: "))
if cilindraje < 125:
    print("Licencia A1")
elif cilindraje <= 499: # Aquí evaluamos que llegue hasta 499 inclusive
    print("Licencia A2")
else:
    print("Licencia A3")

'''Solicita el nivel de dos Pokémon. 
Si el primero tiene mayor nivel, muestra la suma de ambos niveles. Si el segundo es mayor, 
muestra la diferencia (el mayor menos el menor). Si son iguales, informa 'Niveles idénticos'''

nivel_pokemon1=int(input("Que nivel tiene el pokemon1 ?: "))
nivel_pokemon2=int(input("Que nivel tiene el pokemon 2? :"))
suma_niveles = nivel_pokemon1 + nivel_pokemon2
diferencia_niveles = nivel_pokemon1 % nivel_pokemon2
if nivel_pokemon1 > nivel_pokemon2:
    print(suma_niveles)
elif nivel_pokemon2 > nivel_pokemon1:
    print(diferencia_niveles)
else:
    print("Niveles identicos")