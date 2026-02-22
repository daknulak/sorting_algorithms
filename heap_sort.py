import time
import pickle

def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[l] > arr[largest]: largest = l
    if r < n and arr[r] > arr[largest]: largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1): heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

with open('data.pkl', 'rb') as f: datasets = pickle.load(f)

print("KẾT QUẢ HEAP SORT")
for name, data in datasets.items():
    arr = data.tolist()
    start = time.time()
    heap_sort(arr)
    print(f"{name}: {(time.time() - start) * 1000:.2f} ms") 