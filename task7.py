import numpy as np


def counting_sort(data, min_number, max_number):
    n = max_number - min_number + 1  # [0, n]
    counters = [0] * n

    for v in data:
        counters[v - min_number] += 1

    result = []
    for v, count in enumerate(counters):
        result.extend([v + min_number] * count)

    return result

if __name__ == "__main__":
    N = 10000000
    arr = np.random.randint(13, 26, N)
    print(arr[:10])
    print(counting_sort(arr, 13, 26)[:20])