def schitalka(n: int, k: int) -> int:
    spis = [i+1 for i in range(n)]
    spis2 = spis.copy()

    while len(spis) > 1:
        if k > len(spis):
            vik = k % len(spis)
        else:
            vik = k
        print(spis)
        print(vik, spis[vik - 1])
        del spis[vik - 1]

    poslednii = spis[0]
    index = None

    for i in range(len(spis2)):
        if poslednii == spis2[i]:
            index = i
            break
    return index

if __name__ == "__main__":
    print(schitalka(5, 3))
    # n = 5
    # k = 3  # "эники бэники ели вареники, эники бэник ба"
    # spis = [1, 2, 3, 4, 5]
    # spis2 = spis.copy()
    #
    # while len(spis) > 1:
    #     if k > len(spis):
    #         vik = k % len(spis)
    #     else:
    #         vik = k
    #     print(spis)
    #     print(vik, spis[vik - 1])
    #     del spis[vik - 1]
    #
    # poslednii = spis[0]
    # index = None
    # for i in range(len(spis2)):
    #     if poslednii == spis2[i]:
    #         index = i
    #         break
    # print(index+1)
