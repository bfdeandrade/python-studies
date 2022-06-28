from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu_cafe = Menu()
maquina_cafe = CoffeeMaker()
money_machine = MoneyMachine()

valido = True 
while valido:
    
    options = menu_cafe.get_items()
    tipo = input(f"What would you like? ({options}): ")

    if tipo in 'off':
        print('Shutdown machine')
        valido = False
    elif tipo in 'report':
        maquina_cafe.report()
        money_machine.report()
    else:
        pedido = menu_cafe.find_drink(tipo)
        if maquina_cafe.is_resource_sufficient(pedido):
            if money_machine.make_payment(pedido.cost):
                maquina_cafe.make_coffee(pedido)
                
               

