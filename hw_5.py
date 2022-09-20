import time
from multiprocessing import Pool,cpu_count


def factorize(*number):
    # YOUR CODE HERE
    list_with_sets = []
    term=[]
    for i in number:
        for j in range(i+1):
            if i%(j+1)==0:
                term.append(j+1)
        list_with_sets.append(term)
        term = []
    return list_with_sets
if __name__ == "__main__":
    start = time.time()
    a, b, c, d  = factorize(128, 255, 99999, 10651060)
    finish = time.time()
    print(f"time without processes: {finish-start} seconds")
    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]

    start = time.time()
    with Pool(cpu_count()) as pool:
        # print(pool.map(factorize, (128, 255, 99999, 10651060)))
        a,b,c,d = pool.map(factorize, [128, 255, 99999, 10651060])
    finish = time.time()
    print(f"time with {cpu_count()} processes: {finish-start} seconds")
    
            
    assert a[0] == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b[0] == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c[0] == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d[0] == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]