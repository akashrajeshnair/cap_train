import pytest
def image(a):
    res = a

    for o in range(len(res[0])):
        res[o]=res[o][::-1]

    for j in range(0, len(res)):
        for g in range(0, len(res[0])):
            if res[j][g] == 0:
                res[j][g] = 1
            else:
                res[j][g] = 0

    return res
    # for i in range(0, res):
    #     for j in range(0, len(res[0])):
    #         print(res[i][j], end=" ")
    #     print()

def test_image():
    assert image([[0,1], [1,0]]) == [[0,1],[1,0]]