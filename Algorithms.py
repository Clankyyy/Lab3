def mergesort(arr):
    if len(arr) <= 1:
        return arr

    # Split the input array into two halves
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = mergesort(left)
    right = mergesort(right)

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result



def bucketsort(arr):
    # Find the minimum and maximum values in the input array
    min_val = min(arr)
    max_val = max(arr)

    # Calculate the range of values and the number of buckets
    bucket_range = (max_val - min_val) / len(arr)
    num_buckets = len(arr) + 1

    # Create empty buckets
    buckets = [[] for i in range(num_buckets)]

    # Distribute elements into buckets
    for num in arr:
        index = int((num - min_val) / bucket_range)
        buckets[index].append(num)

    # Sort each bucket (using another sorting algorithm or recursively with bucket sort)
    sorted_arr = []
    for bucket in buckets:
        if bucket:
            sorted_arr.extend(sorted(bucket))

    return sorted_arr