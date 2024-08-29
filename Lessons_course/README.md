# PYTHON-AVANZADO
Repo for python avanzado training

El proyecto se encarga de administrar un inventario con varias funciones mostradas en un menu.

Despues de correr el archivo llamado proyecto_1.py el siguiente menu será mostrado:

Nota despues de entrar a cada opción del menu, será regresado al siguiente menú:

-- Item Management System ---
1. Add New Item
2. Update amounts
3. Search Items
4. Sort Items
5. Delete Item
6. Inventory management
7. Inventory statistics
8. Display items by type
10. Exit


Opcion 1. Add New Item.

Para empezar a cargar artículos en el inventario hay que meter la opcion 1. (Add New Item). 

Se le pedirá seguir las instrucciones en la pantalla para introducir los siguientes datos:
name, quantity, unit price, type and size. Despues de ingresar los datos mostrados anteriormente, se mostrará el artículo agregado y el timestamp de cuando el artículo fue agregado como se muestra continuación:

Enter your choice: 1
Adding item

Enter the item name: cocacola
Enter the quantity of the item cocacola: 10
Enter the unit price of the item cocacola: 5.0
Enter the type of the item cocacola: beverage
Enter the size of the item cocacola: small
Item added.
Info of the item:  {'name': 'cocacola', 'amount': '10', 'unit price': '5.0', 'type': 'beverage', 'size': 'small', 'timestamp': '2023/7/11 19:36:26'}

All the items in inventory:  [{'name': 'cocacola', 'amount': '10', 'unit price': '5.0', 'type': 'beverage', 'size': 'small', 'timestamp': '2023/7/11 19:36:26'}]


Opcion 2. Update amounts

Para poder modificar el artículo agregado, puede entrar a la opcion "2. Update amounts" ingresando el número 2.
Despues seguir las instrucciones de la pantalla donde primero pide poner el nombre del articulo que desea modificar, despues ingresar los nuevos datos del artículo.

Después de modificar los valores mostrará el valor modificado. El unico dato que no se modifica es el timestamp del articulo de cuando el articulo fue agregado por primera vez.


Enter your choice: 2
Updating item

Enter the item name to update: cocacola
Enter the new name: Agua
Enter the new quantity: 100
Enter the new unit price: 20.0
Enter the new type: beverage
Enter the new size: medium
Item updated.
Info of the item:  {'name': 'Agua', 'amount': '100', 'unit price': '20.0', 'type': 'beverage', 'size': 'medium', 'timestamp': '2023/7/11 19:36:26'}

All the items in inventory:  [{'name': 'Agua', 'amount': '100', 'unit price': '20.0', 'type': 'beverage', 'size': 'medium', 'timestamp': '2023/7/11 19:36:26'}]

Opcion 3. Search Items

Para poder buscar un articulo dentro del inventario. Hay que ingresar el número 3. Despues aparece un submenú mostrando el criterio de busqueda. Como el siguiente que es mostrado despues del texto: "Search by:". Despues de ingresar el criterio de busqueda, seguir las instrucciones de la pantalla para buscar el articulo con los datos del mismo. Despues de hacer la busqueda aparecera la lista con el artículo hallado.


Enter your choice: 3
Searching item

Search by:
1. Item name
2. Item amount
3. Item unit price
4. Item type
5. Item size
Enter Option: 1
Enter item name to search: Agua
Search results:
Items found: [{'name': 'Agua', 'amount': '100', 'unit price': '20.0', 'type': 'beverage', 'size': 'medium', 'timestamp': '2023/7/11 19:36:26'}]

Opcion 4. Sort Items

Para poder ordenar los articulos del inventario. Hay que ingresar el número 4. Despues aparece un submenú mostrando el criterio de ordenar el inventario. Como el siguiente que es mostrado despues del texto: "Sort by:". Despues de ingresar el criterio de ordenamiento, aparecera la lista con los articulos ordenados por el criterio seleccionado.


Enter your choice: 4
Sorting item
Sort by:
1. Item name
2. Item amount
3. Item unit price
4. Item type
5. Item size
Enter option: 1
Sorted items:
[{'name': 'Agua', 'amount': '100', 'unit price': '20.0', 'type': 'beverage', 'size': 'medium', 'timestamp': '2023/7/11 19:36:26'}]


Opcion 5. Delete Item

Para poder eliminar los articulos del inventario, hay que ingresar el número 5. Despues el programa pedirá ingresar el nombre del artículo. Despues de ingresarlo, aparece el articulo y despues aparecera un mensaje para confirmar si desea borrar el artículo. Al ingresar 1, el artículo será borrado.


Enter your choice: 5
Deleting item
Enter item name to delete: Agua
Item to delete: [{'name': 'Agua', 'amount': '100', 'unit price': '20.0', 'type': 'beverage', 'size': 'medium', 'timestamp': '2023/7/11 19:36:26'}]
Confirm by pressing 1 to delete: 1
Deleting name Agua
Item deleted.

Opcion 6. Inventory management

La opcion de Inventory management tiene 2 opcines de admisnistracion mostradas como en el submenu de abajo.

Para entrar a la opcion de 1. Calculate the total inventory value, ingresar el numero 1.
Nota: Al menos debe de haber un artículo en el inventario para que la funcion pueda trabajar.


Enter your choice: 6

Inventory management
1. Calculate the total inventory value
2. Display available items
Enter the management option: 

Al ingresar la opcion 1 en seguida se calculará el valor total del inventario multiplicando la cantidad por el precio unitario de cada articulo y al final sumando la multiplicación de cada articulo.

Enter the management option: 1
Inventory value:  50.0

Para entrar a la opcion de 2. Display available items, ingresar el numero 2.

Despues de ingresar la opcion 2, aparece otro submenu para mostrar los articulos por 2 criterios, nombre y tipo. Presionar 1 para mistrar la lista de articulos por el nombre.

Enter the management option: 2
1. Display all the items available by name
2. Display all the types availables
Enter the display option: 1
['coca']


Opcion 7. Inventory statistics

Para usar la función 7. Inventory statistics, hay que ingresar el numero 7. Despues un submenu será moistrado, preguntanso si calcular las estadisticas de las cantidades o del dinero de todos los artículos. El ejemplo será mostrado abajo.

Nota: Para que esta función funcione necesita haber al menos 2 articulos en el inventario.

Enter your choice: 7

Show inventory statistics
1. Amounts statistics
2. Money statistics
Enter the statistics option: 1
All the amounts per item:  [5, 10]
The mean of the items amounts:  7.5
The median of the items amounts:  7.5
The standard deviation of the items amounts:  3.5355339059327378


Opcion 8. Display items by type

Para usar la funcion 8. Display items by type, hay que ingresar el numero 8. Despues el programa mostrará todos los tipos que hay disponibles en el inventario. Para continuar el habra que ingresar uno de los tipos mostrados en la lista. Al ingresarlo se mostrara una lista con el tipo ingresado anteriormente.

Enter your choice: 8

Display items by type
['beverage', 'food']
Enter the expected type to search from the options above: food
List of items by type food: ['galleta']


Opcion 10. Exit

La ultima opcion es la funcion 10. Exit, donde al ingresar el numero 10, se terminara el programa.
