import numpy as np
import pickle

def create_datasets():
    datasets = {}
    N = 1000000 # 1 triệu phần tử

    datasets['data_1'] = np.sort(np.random.uniform(-1000, 1000, N))
    datasets['data_2'] = np.sort(np.random.uniform(-1000, 1000, N))[::-1]

    for i in range(3, 6):
        datasets[f'data_{i}'] = np.random.uniform(-1000, 1000, N)

    for i in range(6, 11):
        datasets[f'data_{i}'] = np.random.randint(-1000000, 1000000, N)

    with open('data.pkl', 'wb') as f:
        pickle.dump(datasets, f)

    print("Đã tạo xong")

create_datasets()