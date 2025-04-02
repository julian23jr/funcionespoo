#creacion de super clase animal
class Animal:
    #definir metodo "sonido"
    def sonifo(self):
        pass

#creacion de la sub clase 1, junto con su metodo y atributo
class perro(Animal):
    #se asigna el mismo metodo de la super clase "animal"
    def sonido(self):
        return "guau"

#creacion de la sub clase 2, junto con su metodo y atributo
class gato (Animal):
    #se asigna el mismo metodo de la super clase "animal"
    def sonido(self):
        return "miau"

#creacion de la funcion hacer "sonido"
def hacer_sonido(animal:Animal):
    print(animal.sonido())

#creacion de los objeto
perro=perro()
gato=gato()

#salida de los objetos
Hacer_sonido(perro) 
Hacer_sonido(gato)
