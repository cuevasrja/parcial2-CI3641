#include <iostream>

/**
 * Merge two sorted arrays
 * @param arr array to merge
 * @param l left index
 * @param m middle index
 * @param r right index
 * @return void
 */
void merge(int arr[], int l, int m, int r){
    // Get the sizes of the two arrays
    int n1 = m - l + 1;
    int n2 = r - m;

    int L[n1], R[n2];

    // Copy the data to the two arrays
    for (int i = 0; i < n1; i++){
        L[i] = arr[l + i];
    }

    for (int i = 0; i < n2; i++){
        R[i] = arr[m + 1 + i];
    }

    int i = 0;
    int j = 0;
    int k = l;

    // Merge the two arrays
    while (i < n1 && j < n2){
        if (L[i] <= R[j]){
            arr[k] = L[i];
            i++;
        } else {
            arr[k] = R[j];
            j++;
        }
        k++;
    }

    // Copy the remaining elements of L[] and R[]
    while (i < n1){
        arr[k] = L[i];
        i++;
        k++;
    }

    while (j < n2){
        arr[k] = R[j];
        j++;
        k++;
    }
}

/**
 * Merge sort
 * @param arr array to sort
 * @param l left index
 * @param r right index
 * @return void
 */
void mergeSort(int arr[], int l, int r){
    // If the left index is greater or equal to the right index, return
    if (l >= r){
        return;
    }

    // Get the middle index
    int m = l + (r - l) / 2;
    // Sort the two halves
    mergeSort(arr, l, m);
    mergeSort(arr, m + 1, r);
    // Merge the two halves
    merge(arr, l, m, r);
}

/**
 * Merge sort caller
 * @param arr array to sort
 * @param n size of the array
 * @return void
 */
void mergeSortCaller(int arr[], int n){
    mergeSort(arr, 0, n - 1);
}

/**
 * Print an array
 * @param A array to print
 * @param size size of the array
 * @return void
 */
void printArray(int A[], int size){
    printf("[ ");
    for (int i = 0; i < size; i++){
        printf("%d ", A[i]);
    }
    printf("]\n");
}

int main(int argc, char const *argv[])
{
    if (argc < 2){
        return 1;
    }

    int n = argc - 1 ? atoi(argv[1]) : 0;
    int arr[n];

    for (int i = 0; i < n; i++){
        arr[i] = atoi(argv[i + 1]);
    }

    printf("\033[93mUnsorted\033[0m ");
    printArray(arr, n);

    mergeSortCaller(arr, n);

    printf("\033[92mSorted\033[0m ");
    printArray(arr, n);

    return 0;
}
