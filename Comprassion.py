import timeit
import Algorithms
from main import rastsort, quicksort

A = [234, 43525, 23, 234, 12, 67, 0.232, -32, 0.00000032, 25, 3424234, 98, -12394, 0, 0, 1.2]


merge_sort = timeit.Timer(lambda: Algorithms.merge_sort(A)) 
bucket_sort = timeit.Timer(lambda: Algorithms.bucket_sort(A)) 
quick_sort = timeit.Timer(lambda: quicksort(A))
rast_sort = timeit.Timer(lambda: rastsort(A))

print("merge sort exec time: ", merge_sort.timeit(10))
print ("bucket sort exec time: ", bucket_sort.timeit(10))
print ("quick sort exec time: ", quick_sort.timeit(10))
print ("rast sort exec time: ", rast_sort.timeit(10))
