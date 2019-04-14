#Para ejecutar el script primero se guarda (ctrl + s) y luego (ctrl + b)
#Tools->Build
"""
def nombre_funcion(parametro):
	instruccion
	return (opcional)

"""
#Declaracion de la funcion
def mensaje():
	print("Hola")	#Lineas identadas son el cuerpo de la funcion
	print("a todos")
	print("Soy una funcion :D")

#Ejemplo de una funcion sin argumentos y sin return
#Si la funcion no es llamda, no realizara las acciones
#Llamada de la funcion
mensaje()
print("La ejecucion de las instrucciones es de arriba para abajo")
mensaje()
#Paso de paramatros a las funciones

def suma2():
	num1 = 5
	num2 = 7
	print(num1 + num2)

def suma(numero_1,numero_2):
	print(numero_1 + numero_2)
#numero_1 y numero_2 son parametros
#No se permiten 2 funciones con el mismo nombre, a pesar de que una reciba parametros y el otro no

suma2()
#Si la funcion esta definida con parametros, debes darle esos argumentos para que funcione
#respetando el orden

suma(2,3)
suma("Hola"," Erick")

#Funciones que retornan un valor
def suma3(num1,num2):
	resultado = num1 + num2
	return resultado

#Cuando devolvemos un valor, debe estar guardada en una variable
print(suma3(100,50))

resultado_suma = suma3(100,400)
print(resultado_suma)

#Python pasa los valores por referencia, no por valor TODO son referencias para Python