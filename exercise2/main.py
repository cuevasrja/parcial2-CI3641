from typing import Tuple
from utils.eval import eval
from utils.show import show

def menu() -> Tuple[int, str]|int:
    """
    ### Description
    Show a menu with the available options and return the selected option.

    ### Returns
    - 1: If the user selected the EVAL option.
    - 2: If the user selected the MOSTRAR option.
    - 3: If the user selected the EXIT option.
    - 0: If the user selected an invalid option.
    """
    print("1. EVAL <orden> <expresion>")
    print("2. MOSTRAR <orden> <expresion>")
    print("3. EXIT")
    print("Ingrese una opcion: ")
    in_put = input()
    if in_put.lower().startswith("eval"):
        return (1, in_put[5:])
    elif in_put.lower().startswith("mostrar"):
        return (2, in_put[8:])
    elif in_put.lower() == "exit":
        return 3, ""
    else:
        return 0, ""

def main():
    option = 0
    # While the user does not select the EXIT option
    while option != 3:
        # Show the menu and get the selected option
        option, command = menu()
        # If the option is EVAL, evaluate the expression
        if option == 1:
            order, expression = command.split(" ", 1)
            res = eval(order, expression)
            print(res if res else "Opcion invalida")
        # If the option is MOSTRAR, show the expression in infix notation
        elif option == 2:
            order, expression = command.split(" ", 1)
            res = show(order, expression)
            print(res if res else "Opcion invalida")
        # If the option is EXIT, print a message
        elif option == 3:
            print("Saliendo...")
        # If the option is invalid, print a message
        else:
            print("Opcion invalida")

if __name__ == "__main__":
    main()