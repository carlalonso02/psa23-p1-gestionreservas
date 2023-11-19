# psa23-p1-gestionreservas
El archivo a corregir es la version 'evaluable' de 'codgio_def.py'
# Funcionamiento de la practica
Para comenzar llamo a los dos csv, el de clase businness y el regular, (db, dr respectivamente).
Para trabajar mas facilmente con la funciones, los uno en un solo dataframe, dt.

DIBUJO DEL AVION
Para realizar el dibujo necesito saber que asientos estan libres y cuales no, y para ello tambien necesito saber todas las posibles combinaciones de asientos. Asi ademas puedo dibujar todos los asientos. 
Creo una lista que se llama sitios, en esta lista voy a introducir usando dos bucles todas las posibles combianciones de asientos. Un bucle recorre las filas, que va de 1 a 21, y otro recorre las letras 'ABCDEF'. De esta forma obtengo una lista que tiene datos de este tipo: ['1A', '1B', '1C', '1D',1E', '1F', '2A',......'20F']
Una vez tengo esa lista, creo otra lista con los sitios reservados, para ello uso el dataframe dt, que ya cuenta con db y dr; pero uso solo la columna de 'Asientos'. Tendra la misma forma que la anterior pero solo contendra los asientos reservados.

Para asiganr las letras 'R' o 'L' uso un bucle que recorra todas las fila y las imprima en pantalla. Dentro de este bucle creo otros dos, pero que estan divididos en 'ABC' y 'DEF' para crear asi las dos columnas de asientos del avion. Dentro de cada uno de estos bucles 'for' uso un 'if else'. Si alguno de los asientos que estan en la lista sitio esta tambien en la lista asientos_reservados, escribe en pantalla una 'R' de reservado, si no esta (else), escribe una 'L'. De esta forma ya tengo el dibujo del avion, que ademas al trabajar directamente con la informacion de los csv, si esta informacion se modifica, el dibujo tambien.

INFO GENERAL
Porcentaje del vuelo ocupado:
Para ello calculo el numero de filas en el el dataframe dt usando '.shape' ,las divido entre 120 asientos, luego lo multiplico por 100 y tengo el porcentaje de ocupación.

Numero de pasajeros alojados en cada clase:
Para realizar esta parte de la practica volvi a usar '.shape' para contar el numero de filas de cada archivo csv, y con el numero de filas tengo el numero de pasajeros que ocupa cada clase. 

Numero de pasajeros que facturan su maleta:
Creo una funcion que recorra la columna de facturacion de dt y si se encuentra con que el dato empeiza por 'S', de 'si' lo contabilizo. Añado el comando 'strip' para eliminar los espacios en blanco por si hubiese alguno.

MENU
He creado primero una serie de funciones que solo imprimiran en pantalla informacion: el menu, las opciones de ordenar la informacion de los pasajeros y las opciones de asiento. Tienen la forma 'print_...()'

Despues cree otra serie de funciones que piden al usuario elegir entre varias opciones: clase business o regular, las funciones del menu, forma de ordenar la informacion, y la preferencia de asiento 'op_...()'

Para mostrar la informacion de las reservas cree una funcion (info_reservas) que llama a 'op_clases()' y trabaja con el input de esta. Si se elige una clase u otra muestra en pantalla ese csv.

A continuacion de esta funciones se encuntra 'orden_num(asiento)'. Cree esta funcion que usa el modulo 're' de python para separar los numeros de las letras que forman cadenas, la usare en la funcion que ordena la información de los pasajeros.

Para mostrar la informacion de las reservas llamo a 'info_reservas(db,dr)'. Esta funcion tan solo muestra en pantalla el csv solicitado.

Para mostrar la información de los pasajeros cree 'info_pasajeros(db,dr)'. Lo primero que hace es preguntar al usuario como quiere ordenar la informacion, si es alfabaeticamente o numericamente. Una vez ya sabe como ordenar la informacion pregunta de que clase se quiere ver la informacion, de esta forma sabe a que dataframe llamar. Para ordenar alfabeticamente ordeno todo el dataframe seleccionando en funcion de la columna 'Apellidos'. Para ordenarlo numericamente llamo a 'orden_num' usando '.apply' que ejecuta la funcion a lo largo de la columna que yo elija, que en este caso me interesa aplicar en 'Asiento'. Esta funcion, genera una nueva columna llamada 'Numeros', esta formada por los numeros de los asientos que hemos extraido, y es la que usare para ordenar la informacion. Pero despues de ordenarla, elimino esa columna que no usare más.

Antes de añadir una nueva reserva necesito saber que sitios estan disponibles, para ello creo la funcion 'buscar_sitio()'. Esta funcion trabaja con preferencia, que viene de elegir donde prefiere sentarse el usuario; con la lista sitios y asietos reservados, y eleccion que viene de la clase en la que se quiere añadir la reserva. 
Para comenzar, la funcion le pregunta al usuario su clase, ya que en funcion de esta se trabajara en un rango de filas u otro. Una vez se sabe en que rango trabajar se vuelve a usar la lista sitios, en la que estaban todos los asientos del avion y se recorre con un bucle y separando nuevamente los numeros de las letras; pero en funcion de la clase debe cumplir que sea o bien menor o igual que 8, o mayor que 8. Los numeros de la lista que cumplen esto se agrupan mediante '.group()' y ya se tienen separados asientos business de regular.
Despues en funcion de la preferencia de sitio introducida por el usuario se le ponen condiciones a los asientos en funcion de las letras que contengan y se crea una nueva lista que contiene las preferencias.
Para finalizar la funcion, como lo que se busca son asientos libre, con un bucle 'for', si no se encuntran un asiento de las listas de preferencia en la lista de asientos reservados, se devuelve ese asiento; si coincide con alguno, no devuelve nada ya que ese asiento esta ocupado por otra persona.

Tambien es necesario la informacion del usuario, creo 'info_usuario()'. Esta funcion primero comprueba que el dni no esta en uso buscandolo en el dataframe dt. Si esta en uso da un mensaje y vuelve al menu principal. Si no lo esta le pide al usuario introducir la informacion relevante a la reserva.

Para terminar de añadir la reserva, esta 'add_reserva()'. La funcion trabaja en funcion de condiciones, si recibe un asiento de la funcion 'buscar_sitio()' llama a funciones anteriores que le daran la informacion para guardar la reserva, entre lo que recibe esta el asiento disponible, que lo añadira a la lista de asientos reservados para que deje de estar disponible. En funcion de este numero de asiento se decide a que dataframe enviar la informacion introducida. Para acortar el codigo, primero guardo la reserva en el dataframe dt, y en funcion de ese numero de asiento se envia la informacion y se guarda al csv correspondiente. Si al comienzo de todo no recibe un asiento, significa que no hay asientos disponibles asi que esa clase esta completa, vuelve al menu principal.

Para modificar una reserva primero necesito saber que reserva modificar. Como cada reserva esta asociada a un dni creo la funcion 'buscar_dni()'. Esta funcion le pide al usuario que introduzca su dni, despues lo busca en el dataframe total y si no esta no hay reserva que modificar asi que vuelve al menu principal. Si si que encuentra el dni es lo que devuelve para usar en la funcion de modificar.

La funcion que modifica el asiento es 'mod_reserva()'  
[esta funcion pide varias veces al usuario introducir su dni y clase, no se como evitar que se repita tanto  estas peticiones sin provocar fallos. Tambien genera un mensaje con tradictorio pero guarda correctamente el nuevo asiento] 
Lo primero que hace es pedir el dni al usario, al que estara asociado la reserva, tambien pide la clase en la que esta la reserva y la nueva preferencia de asiento; ademas llamara a 'buscar_sitio()'. Si de esta ultima funcion recibe un sitio, continua ejecutando la funcion. Tras esto lee los archivos csv pero especificando que la columna 'DNI' sea una cadena, despues en estos "nuevos" dataframe se busca del dni introudcido por el usuario, si se encuentra en cada dataframe seleccionado se modifica el valor de la columna 'Asiento' para esa fila y se guarda en el csv; si no encuentra nada lo comunica y vuelve al menu principal.

Para eliminar una reserva esta 'elim_reserva()'. Que pide al usuario la clase en la que se encuentra y su dni para  buscar la reserva. Una vez encuentra la fila a la que pertenece el dni en el dataframe seleccionado la elimina y guarda el archivo.

Finalmente, para el menu esta 'menu()' que mediante un bucle while se ejecutara de forma continua hasta que el usario decida salir y cambie la variable boolena 'salir' a True. En funcion de lo que eliga el usuario llamara a una funcion de las descritas anteriores o a otras.
# Cuestiones
La programación orientada a objetos es un tipo de programación que trabajara con objetos, que son instancias de clases.
Una clase es una forma de agrupar datos y acceder a ellos de forma sencilla. Tambien puede verse como una plantilla que usamos para la creacion de nuevos datos.
Una instancia es un objeto creado desde una clase.
Podremos usar funciones y metodos para trabajar con las instancias.

Para esta practica se podria usar POO crando una clase para la categoria business y otra para la regular, y que con metodos y funciones mostrase la informacion pedido o midificase las reservas.

La principal diferencia entre una función y un método es que la función trabaja con datos externos a ella, mientras que el metodo tan solo necesita los atributos, caracteristicas propias, de la clase en la que esta definida para trabajar correctamente y ademas siempre estara dentro de la clase, definido junto a aella. Mientras que la funcion podra estar tanto dentro como fuera.

Un constructor es un método que sirve para inicializar los atributos de forma automatica. El cosntructor tiene la siguiente llamada: __init__(self). 
No necesita tener parametros ya que cuando creamos una clase no se requiere proporcionar un valor especifico para su creacion, con "self" sirve; auqnue se podrian añadir parametros si el objetivo del programa lo requiriese.

Tanto las listas como los diccionarios son estrcutras de datos, pero las listas son una secuencia ordenadas de elementos, se accede a estos elementos mediante un indice que comienza en cero y se define entre corchetes []. 
Un diccionario no esta ordenado igual que una lista, esta formado por parejas de clave-valor; a sus elementos se acceden mediante esas claves y de esta forma obtiene el valor asociado a esa clave, que es exclusiva del valor; y se define entre llaves {}. 
Tanto las listas como los diccionarios se pueden modificar, pero las listas se usan cuando quieres tener datos ordenados segun un indice, mientras que los diccionarios asocian datos a claves con las que obtener esos datos.

Para usar listas y diccionarios en la practica se podrian guardar cada csv en una lista distinta, y para modificar los asientos o reservas, usar diccionarios accediendo a las filas mediante claves especificas, por ejemplo el dni, que es unico para cada reserva. 

