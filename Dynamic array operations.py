# Dynamic array operations
# https://www.hackerrank.com/challenges/dynamic-array/problem


def dynamicArray(n, queries):
    seqList = [[] for _ in range(n)]
    lastAnswer = 0
    result = []

    for query in queries:
        q_type, x, y = query
        idx = (x ^ lastAnswer) % n

        if q_type == 1:
            seqList[idx].append(y)
        elif q_type == 2:
            lastAnswer = seqList[idx][y % len(seqList[idx])]
            result.append(lastAnswer)

    return result


if __name__ == '__main__':
    n, q = map(int, input().split())

    queries = [list(map(int, input().split())) for _ in range(q)]

    results = dynamicArray(n, queries)

    for ans in results:
        print(ans)
