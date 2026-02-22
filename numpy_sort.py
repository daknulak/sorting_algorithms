import time
import pickle
import numpy as np

with open('data.pkl', 'rb') as f:
    datasets = pickle.load(f)

print("KẾT QUẢ NUMPY SORT")
for name, data in datasets.items():
    arr_for_numpy = data.copy()
    start = time.time()
    np.sort(arr_for_numpy)
    print(f"{name}: {(time.time() - start) * 1000:.2f} ms")
