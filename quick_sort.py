import time
import pickle
import sys

sys.setrecursionlimit(2500000)

def partition(arr, low, high):
    mid = (low + high) // 2
    arr[mid], arr[high] = arr[high], arr[mid]
    # -----------------------------------------

    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort(arr, low, high):
    if low < high:
        p = partition(arr, low, high)
        quick_sort(arr, low, p - 1)
        quick_sort(arr, p + 1, high)

# Đọc dữ liệu và chạy test
with open('data.pkl', 'rb') as f: 
    datasets = pickle.load(f)

print("KẾT QUẢ QUICK SORT")
for name, data in datasets.items():
    arr = data.tolist()
    try:
        start = time.time()
        quick_sort(arr, 0, len(arr) - 1)
        print(f"{name}: {(time.time() - start) * 1000:.2f} ms")
    except RecursionError:
        print(f"{name}: Lỗi đệ quy (Do mảng đã sắp xếp)")
    except Exception as e:
        print(f"{name}: Lỗi khác - {e}")