import math

def find_fibonacci(n):
    if n < 1:
        return -1
    if n == 1:
        return 0
    if n == 2:
        return 1
    
    return find_fibonacci(n - 1) + find_fibonacci(n - 2)

def is_perfect_square(x):
    s = int(math.sqrt(x))
    return s ** 2 == x

def is_fibonacci(f):
    return is_perfect_square(5 * f ** 2 + 4) or is_perfect_square(5 * f ** 2 - 4) 

def find_index(n) :
    if n <= 1:
        return n
  
    a = 0
    b = 1
    c = 1
    res = 1
  
    while c < n:
        c = a + b
        res = res + 1
        a = b
        b = c
         
    return res

if __name__ == '__main__':
    print(find_index(4))