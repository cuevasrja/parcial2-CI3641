import sys

def sort(lista):
    """
    ### Description:
    This function sorts a list of integers in ascending order using the selection sort algorithm.

    ### Arguments:
    - lista: list of integers to be sorted.

    ### Returns:
    A generator that yields the elements of the list in ascending order.
    """
    while lista:
        # Find the index of the minimum element
        min_index = min(range(len(lista)), key=lista.__getitem__)
        # Remove the minimum element from the list and return it
        yield lista.pop(min_index)

def main():
    lista = list(map(int, sys.argv[1:]))

    for x in sort(lista):
        print(x, end=" ")

    print()

if __name__ == "__main__":
    main()