def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Get the number of students from the user
n = int(input("Enter the number of students: "))

# Get the marks from the user
marks = []
for i in range(n):
    mark = int(input(f"Enter the mark for student {i+1}: "))
    marks.append(mark)

# Sort the marks using QuickSort
sorted_marks = quick_sort(marks)

# Print the sorted list of marks
print("List after sorting is:", sorted_marks)

