def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

def count_occurrences(arr, target):
    count = 0
    for element in arr:
        if element == target:
            count += 1
    return count

# Get the input array from the user
array = list(map(int, input("Enter the integer array: ").split()))

# Sort the array
sorted_array = sorted(array)

# Print the sorted array
print("Sorted array:", sorted_array)

# Get the element to search from the user
element = int(input("Enter the element to search: "))

# Search the element using binary search
index = binary_search(sorted_array, element)

if index != -1:
    # Count the occurrences of the element
    occurrences = count_occurrences(sorted_array, element)
    print(f"Number of occurrences of element {element} is: {occurrences}")
else:
    print("Element not found in the array.")

