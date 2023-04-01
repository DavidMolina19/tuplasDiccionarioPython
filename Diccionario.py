"""diccionario={} formas de crear diccionario
diccionario= dict()"""


# datos={"nombre":"paola","edad":27,"sexo":"m",
#        "fecha":"10/07/90"}
# datos1=dict(nombre="mariana",
#             edad=20,
#             sexo="f",
#             fecha="1/9/2002"
#             )

# #acceder a un elemento
# print(datos["nombre"])

# #modificar un  valor
# datos["nombre"]="mariana"
# datos["sexo"]="f"
# print(datos)

# #metodo get(): devuelve el elemento de la clave
# print(datos.get("edad"))

# #metodo update(): actualizar el diccionario
animales={"invertebrado":"gusano","vertebrado":"pollito","acuatico":"delfin","omnivoro":"raton"}
marcas={"tenis":"adidas","celular":"motorola","carro":"ferrari"}
# marcas.update(animales)
# print(marcas)
# print(animales)

# #metodo pop():eliminar la clave pasada como argumento y su valor
# animales.pop("omnivoro")
# print(animales)

# animales.popitem()
# print(animales)


#imprimir solo claves del diccionario


print(animales.keys())
for clave in animales.keys():
    print(clave)

#imprimir solo valores
print(animales.values())

for atributo in animales.values():
    print(atributo)


#eliminar todos los elementos del diccionario

animales.clear()
print(animales)


for claveVal in marcas.items():
    print(claveVal) 
    
       