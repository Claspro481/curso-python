v = True
f = False
print(v)
print(f)
print(type(v))
print(5 > 3) #true
print(3 > 5) #false


#Ejemplo de como se usan los booleanos 

usuario = "Jostyn"
password = "1234"

#Validacion boolenada 
login_correcto = (usuario == "Jostyn" and password == "1234")
if login_correcto:
    print("Acceso permitido") #True or false 
else:
    print("Acceso denegado")

#Carrito de compras 
carrito = [1]
carrito_vacio = (len(carrito) == 0)
if carrito_vacio:
    print("Tu carro de compras esta vacio")
else:
    print("Tienes productos en tu carrito")

#Validacion por email 
email = "usuario@gmail.com"
es_valido = ("@" in email and "." in email)
if es_valido:
    print("Email valido")
else:
    print("Email invalido")

#Jueo de vida de un  jugador 
vida = 0
jugador_vivo = (vida > 0)
if jugador_vivo:
    print("El juador sigue en la partida")
else:
    print("Game Over")

#App de clima 
#variable que nos retorna el dato
temperatura = 40
#condicion que creamos sobre la temperatura 
hace_calor = (temperatura > 30)
if hace_calor:
    print("Hace calor")
else:
    print("El clima esta normal")
