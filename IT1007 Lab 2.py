#Q1a
def nChooseK(n, k):
    n_factorial = 1
    k_factorial = 1
    nk_max = (n - k)
    nk_factorial = 1
    for i in range(2, n+1):
        n_factorial = i * n_factorial

    for j in range(2, k+1):
        k_factorial = j * k_factorial

    for l in range(2, nk_max+1):
        nk_factorial = l * nk_factorial
    ans = n_factorial / ((k_factorial) * nk_factorial)
    print (ans)

#Q1b
def nChooseK_recursive(n,k):
    if (k==n or k==0):
        return 1
    else:
       return nChooseK_recursive(n-1,k-1) + nChooseK_recursive(n-1,k)


#Q2
import random
from math import sqrt
def monte_carlo_pi(n):
    hit_count = 0
    for i in range(0,n):
        y = random.randint(0, 100)
        x = random.randint(0, 100)
        d = sqrt(y*y + x*x)
        if d <= 100:
            hit_count += 1
    p = hit_count/n
    pi_value = p*4
    print(pi_value)


