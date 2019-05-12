


def rotLeft(a1,d1):

    for i in range(0,d1):
        a1.append(a1.pop(0))
    return a1


if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    print(result)
