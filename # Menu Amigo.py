# Menu Amigo
# Un menu que calcula el total de una orden del usuario(incluye impuesto)
# Realizado por: Jorge Morillo, Shuodi Liang, Pedro García, Andre Delgado
# Fecha: 2024/10/25
# Bibliotecas

# Constantes y variables
order_finish = False #Diciendole al programa que la orden no ha terminado
# El menú
menu = {
    "Entradas": {
         ("Croquetas", 4.50),
         ("Jamón", 5.00),
         ("Calamares", 6.00)
    },
    "Platos principales": {
         ("Pulpo", 15.00),
         ("Empanada de choco", 10.00),
         ("Empanada de atún", 10.00)
    }
}
order = {} #El pedido del usuario, vacio ahora para que el usario lo rellene con los productos que quiera
def show_menu():#define la función
    print("MENÚ")
    for category, itemz in menu.items():#Devuelve todos los valores(productos) de nuestro menu
        print(f"\n{category}:")#fstring que separa los productos por su sección
        for number, (name, price) in itemz.items():#
            print(f"{number}. {name} - ${price:.2f}")


def add_to_order(item_number, section_name):
    if item_number in menu[section_name]:
        name, price = menu[section_name][item_number]
        if name in order:
            order[name] = (price, order[name][1] + 1)
        else:
            #
            order[name] = (price, 1)
        print(f"\n {name} ha sido añadido a tu pedido")
    else:
        print("Ese número no es valido")

def show_order():
    if not order:
        print('No tiene nada en su orden D:')
    return

print('Dentro de tu orden actual')
for name, (price, quantity) in order.items():
    subtotal = 0
    total_item = price*quantity

def Total():
    Tax_Rate = 0.08
    subtotal = total_item+(Tax_Rate*total_item)
def Cancel_Order():
    order.clear()
    print('Su orden a sido cancelada')
# Inicio
def main_menu():
    
    print('Buenos días:')
    print('Que le gustaría hacer')
    print('1: Iniciar pedido')
    print('2:Cancelar pedido')
    user_choice = int(input('Elija una opción: '))
    if user_choice == 1:
        Order = True
        print('Comenzaremos tu pedido brevemente')
        show_menu()
    elif user_choice == 2:
        print('Su pedido ha sido cancelado, que tenga buen día')
        Order = False
    else:
        print('Ese número no es válido, por favor intente de nuevo')
while order == True:

    if order_finish == False:
 
        if 1==1:
            main_menu()
# Fin
