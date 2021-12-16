import time
import numpy as np
import matplotlib.pyplot as plt

def median(numbers):
    min_h = None
    min_value = float('inf')
    for h in numbers:
        total_abs_loss = 0
        for x in numbers:
            total_abs_loss += abs(x - h)
        if total_abs_loss < min_value:
            min_value = total_abs_loss
            min_h = h
    return min_h

n = [100, 400, 700, 1000, 1300, 1600, 1900]
time_list = []

def time_median(n):
    out = 0
    round = 10
    random_numbers = np.random.rand(n)

    for i in list(range(0, round)):
        start = time.time()
        median(random_numbers)
        end = time.time()
        elapsed = end - start
        out += elapsed
    return out / round

if __name__ == '__main__':
    for i in n:
        time_list.append(time_median(i))
    plt.plot(n, time_list)
    new_ticks1 = n
    plt.xticks(new_ticks1)
    plt.show()