def selectionSort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Example usage
if __name__ == "__main__":
    sample_array = [64, 25, 32, 20, 40, 15]
    sorted_array = selectionSort(sample_array)
    print("Sorted array is:", sorted_array)