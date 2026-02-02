def Divide(arr, l , r ):
    if l < r:
        m = (l + r) // 2
        Divide(arr, l, m )
        Divide(arr, m + 1, r)
        Merge(arr, l, m, r)

def Merge(arr, l, m, r):
    s1 = m - l + 1
    s2 = r - m 

    L = [0] * (s1)
    R = [0] * (s2)

    for i in range(0 , s1):
        L[i] = arr[l + i]
    for j in range(0 , s2):
        R[j] = arr[m + 1 + j]
    
    i = j = 0
    k = l

    while (i < s1 and j < s2):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    
    while i < s1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < s2:
        arr[k] = R[j]
        j += 1
        k += 1
    
def mergeSort(arr):
    Divide(arr, 0, len(arr) - 1)
    return arr

# Example usage:
if __name__ == "__main__":
    sample_array = [64, 25, 32, 20, 40, 15]
    sorted_array = mergeSort(sample_array)
    print("Sorted array is:", sorted_array)

