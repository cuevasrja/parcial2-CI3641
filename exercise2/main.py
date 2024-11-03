from typing import Tuple
from utils.eval import eval
from utils.show import show

def menu() -> Tuple[int, str]|int:
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
    while option != 3:
        option, command = menu()
        if option == 1:
            order, expression = command.split(" ", 1)
            res = eval(order, expression)
            print(res if res else "Opcion invalida")
        elif option == 2:
            order, expression = command.split(" ", 1)
            res = show(order, expression)
            print(res if res else "Opcion invalida")
        elif option == 3:
            print("Saliendo...")
        else:
            print("Opcion invalida")

if __name__ == "__main__":
    main()