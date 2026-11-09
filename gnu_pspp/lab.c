#include <stdio.h>

#include <time.h>

 

// Function to implement binary search

int binarySearch(int arr[], int low, int high, int key) {

    while (low <= high) {

        int mid = low + (high - low) / 2;

 

        // Check if key is present at mid

        if (arr[mid] == key)

            return mid;

 

        // If key is greater, ignore left half

        if (arr[mid] < key)

            low = mid + 1;

        // If key is smaller, ignore right half

        else

            high = mid - 1;

    }

 

    // Element was not present in the list

    return -1;

}

 

int main() {

    // Pre-defined sorted list of integers

    int arr[] = {10, 20, 30, 40, 50, 60, 70, 80, 90, 100};

    int n = sizeof(arr) / sizeof(arr[0]);

 

    printf("Sorted List of Integers:\n");

    for (int i = 0; i < n; i++) {

        printf("%d ", arr[i]);

    }

    printf("\n\n");

 

    int key;

    printf("Enter the element to be searched: ");

    scanf("%d", &key);

 

    // Measuring time for user search

    clock_t start_time = clock();

    int result = binarySearch(arr, 0, n - 1, key);

    clock_t end_time = clock();

 

    double search_time = ((double)(end_time - start_time)) / CLOCKS_PER_SEC;

 

    // Output result based on search

    if (result != -1) {

        printf("The element is found at location (index): %d (Position: %d)\n", result, result + 1);

    } else {

        printf("The element is not found in the list\n");

    }

    printf("Time taken for this search: %.7f seconds\n\n", search_time);

 

    // --- Best and Worst Case Time Analysis ---

    printf("--- Best and Worst Case Performance Analysis ---\n");

 

    // 1. Best Case: The element is found at the very first comparison (middle element)

    int best_case_key = arr[n / 2];

    clock_t best_start = clock();

    binarySearch(arr, 0, n - 1, best_case_key);

    clock_t best_end = clock();

    double best_time = ((double)(best_end - best_start)) / CLOCKS_PER_SEC;

    

    printf("Best Case (Key: %d found at middle):\n", best_case_key);

    printf(" Execution Time: %.7f seconds\n", best_time);

 

    // 2. Worst Case: The element requires the maximum number of iterations (not present / extreme end)

    int worst_case_key = 999; // Value not in the array

    clock_t worst_start = clock();

    binarySearch(arr, 0, n - 1, worst_case_key);

    clock_t worst_end = clock();

    double worst_time = ((double)(worst_end - worst_start)) / CLOCKS_PER_SEC;

 

    printf("Worst Case (Key: %d not in list, max iterations):\n", worst_case_key);

 

  printf(" Execution Time: %.7f seconds\n", worst_time);

 

    return 0;

}