import sys

def sort(arr):
    """
    ### Description:
    This function sorts a list of integers in ascending order using a recursive approach.

    ### Arguments:
    - arr: list of integers to be sorted.

    ### Returns:
    A generator that yields the elements of the list in ascending order.
    """
    if arr:
        # Find the index of the minimum element
        min_index = min(range(len(arr)), key=arr.__getitem__)
        # Yield the minimum element
        yield arr[min_index]
        # Recursively sort the remaining elements
        yield from sort(arr[:min_index] + arr[min_index+1:])

def main():
    arr = list(map(int, sys.argv[1:]))

    for x in sort(arr):
        print(x, end=" ")

    print()

if __name__ == "__main__":
    main()