
def maxcommon(a, b, n):

    if a*n % b == 0:
        return a*n
    else:
        return maxcommon(a, b, n+1)

if __name__ == "__main__":

    arr = [2, 4, -7, 5, 2, -1, 2, -4, 3]
    a = 36
    b = 21
    print(maxcommon(a, b, 1))