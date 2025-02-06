import multiprocessing as mp
import os
import time
# test comment
def find_prime(n):
    if n in [1, 2, 3]:
        return n

    flag = False
    for i in range(2, n // 2):
        if int(n / i) == n / i:
            flag = True
            break

    if not flag:
        print(f"Process {os.getpid() % 10} found the prime number: {n}")
        # q.put(n)
        return n

if __name__ == '__main__':
    q = mp.Queue()
    with mp.Pool(processes=10) as pool:
        for i in pool.imap_unordered(find_prime, range(1000)):
            pass
