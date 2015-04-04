frutas = ["Manzana","Mango","Uva","Sandia"]

#append -> Agregar un elemento al arreglo
frutas.append("Fresas")

#inser -> Agregar 2 instrucciones, una el elemento y posicion
frutas.insert(2,"Naranja")

#extend -> agregar los elementos de una arreglo a otro arreglo
verduras = ["Lechuga", "Papa", "Zapallo"]
frutas.extend(verduras)

#remove -> remover el elemento del arreglo indicado
frutas.remove("Manzana")

#pop -> remover el elemento segun su posicion
frutas.pop(5)

print frutas