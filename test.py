import multiprocessing as mp
import os
import time
from math import sqrt

def find_prime(n):
    if n in [1, 2, 3]:
        return n

    flag = False
    for i in range(2, round(sqrt(n))):
        if int(n / i) == n / i:
            flag = True
            break

    if not flag:
        print(f"Process {os.getpid() % 10} found the prime number: {n}")
        # q.put(n)
        return n

if __name__ == '__main__':
    tic = time.time()
    q = mp.Queue()
    with mp.Pool(processes=32) as pool:
        for i in pool.imap_unordered(find_prime, range(1_000_000)):
            pass
    toc = time.time()
    time1 = toc - tic

    tic = time.time()
    for i in range(1, 1_000_000):
        find_prime(i)
    toc = time.time()
    time2 = toc - tic

    print(f"It took us {time1} seconds using mp")
    print(f"It took us {time2} seconds without mp")

    print(f"that's a {(time2 / time1) * 100} % difference")

    print(time2 > time1)
