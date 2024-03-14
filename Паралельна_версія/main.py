from multiprocessing import cpu_count, Pool

def factorize(*number):
    with Pool(cpu_count()) as pool:
        factors = pool.map(factorize_single, number)
    return factors

def factorize_single(num):
    factors = [1]
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            factors.append(i)
            if i * i != num:
                factors.append(num // i)
    return factors

    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [
                 1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158,
                 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212,
                 2662765, 5325530, 10651060
                 ]
#Elapsed time: 0.4 sec
