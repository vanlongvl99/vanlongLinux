import sys
sys.setrecursionlimit(10000000)



def unionSet(u, v, total):
    up = findSet(u)
    vp = findSet(v)
    if up == vp:
        return
    if ranks[up] > ranks[vp]:
        parents[vp] = up
        total[up] += total[vp]
    elif ranks[up] < ranks[vp]:
        parents[up] = vp
        total[vp] += total[up]
    else:
        parents[up] = vp
        ranks[vp] += 1
        total[vp] += total[up]


def makeSet():
    global parents, ranks
    parents = [i for i in range(n+1)]
    ranks = [0 for i in range(n+1)]


def findSet(u):
    if u != parents[u]:
        parents[u] = findSet(parents[u])
    return parents[u]



if __name__ == "__main__":
    test = int(input())
    for _ in range(test):
        n, m = map(int, input().split())
        parents = []
        ranks = []
        makeSet()
        total = [1 for i in range(n+1)]
        for _ in range(m):
            u, v = map(int, input().split())
            unionSet(u, v, total)
        print(max(total))

    