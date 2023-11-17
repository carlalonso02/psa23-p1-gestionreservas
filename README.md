# psa23-p1-gestionreservas

# Funcionamiento de la practica
Concepto de estructuras de datos y su uso en la práctica\\
Concepto de prueba unitaria y su uso en la práctica
# Cuestiones
La programación orientada a objetos es un tipo de programación que trabajara con objetos, que son instancias de clases.
Una clase es una forma de agrupar datos y acceder a ellos de forma sencilla. Tambien puede verse como una plantilla que usamos para la creacion de nuevos datos.
Una instancia es un objeto creado desde una clase.
Podremos usar funciones y metodos para trabajar con las instancias.

Para esta practica se podria usar POO crando una clase para la categoria business y otra para la regular, y que con metodos y funciones mostrase la informacion pedido o midificase las reservas.

La principal diferencia entre una función y un método es que la función trabaja con datos externos a ella, mientras que el metodo tan solo necesita los atributos, caracteristicas propias, de la clase en la que esta definida para trabajar correctamente y ademas siempre estara dentro de la clase, definido junto a aella. Mientras que la funcion podra estar tanto dentro como fuera.

Un constructor es un método que sirve para inicializar los atributos de forma automatica. El cosntructor tiene la siguiente llamada: __init__(self). 
No necesita tener parametros ya que cuando creamos una clase no se requiere proporcionar un valor especifico para su creacion, con "self" sirve; auqnue se podrian añadir parametros si el objetivo del programa lo requiriese.

Tanto las listas como los diccionarios son estrcutras de datos, pero las listas son una secuencia ordenadas de elementos, se accede a estos elementos medinte un indice que comienza en cero y se define entre corchetes []. 
Un diccionario no esta ordenado igual que una lista, esta formado por parejas de clave-valor; a sus elementos se acceden mediante esas claves y de esta forma obtiene el valor asociado a esa clave, que es exclusiva del valor; y se define entre llaves {}. 
Tanto las listas como los diccionarios se pueden modificar, pero las listas se usan cuando quieres tener datos ordenados segun un indice, mientras que los diccionarios asocian datos a claves con las que obtener esos datos.

Para usar listas y diccionarios en la practica se podrian guardar cada csv en una lista distinta, y para modificar los asientos o reservas, usar diccionarios accediendo a las filas mediante claves especificas, por ejemplo el dni, que es unico para cada reserva. 

