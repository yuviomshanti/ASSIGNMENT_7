def remove_duplicates(arr):
    return list(set(arr))

def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Get the input array from the user
array = list(map(int(input("Enter the integer array: ").split()))

# Remove duplicates from the array
unique_array = remove_duplicates(array)

# Print the unique array
print("Unique array:", unique_array)

# Sort the array using selection sort
selection_sorted_array = selection_sort(unique_array)

# Print the sorted array using selection sort
print("Sorted array (Selection Sort):", selection_sorted_array)

# Sort the array using bubble sort
bubble_sorted_array = bubble_sort(unique_array)

# Print the sorted array using bubble sort
print("Sorted array (Bubble Sort):", bubble_sorted_array)

