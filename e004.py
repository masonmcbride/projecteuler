# Project euler problem 4
# projecteuler.net/problem=4

def compute():
    ans = max(i*j
        for i in range(100, 1000)
        for j in range(100, 1000)
        if str(i*j) == str(j*i)[::-1])

    return str(ans)


if __name__ == '__main__':
    print(compute())
