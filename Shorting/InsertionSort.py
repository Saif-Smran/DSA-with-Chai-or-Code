def insertionSort(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Move elements of arr[0..i-1], that are greater than key,
        # to one position ahead of their current position
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Example usage:
if __name__ == "__main__":
    sample_array = [64, 25, 32, 20, 40, 15]
    sorted_array = insertionSort(sample_array)
    print("Sorted array is:", sorted_array)