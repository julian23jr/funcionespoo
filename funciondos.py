import random

#realizar funcion probabilidad

def probabilidad (num_lanzamientos,num_caras):
    
    #Simular los lanzamientosde la moneda
    resultado=[random,choice(¨[0,1])] for _ in range(num_lanzamientos)
    
    #Calcular la probabilidad de obtener el numero caras 
    prob=resultados.count(1)/num_lanzamientos
    return prob 

#Ejemplo de uso ( declaracion de objetos)
num_lanzamiento=10
num_caras=6


prob=probabilidad(num_lanzamiento,num_caras)
print(f"la probabilidad de obtener {num_caras} caras en {num_lanzamientos} es{prob:.4f}")
