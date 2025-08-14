def encode(s):
    results = []
    lst = list(s)
    for _ in range(len(lst)):  # rotate once for each element
        lst.insert(0, lst.pop())  # remove last item and insert at front
        results.append("".join(lst))  # append a *copy* so future changes don't overwrite
    results = sorted(results)
    lastCol = ""
    for i, r in enumerate(results):
        lastCol += results[i][-1]
        if r == s:
            index = i
    output = (lastCol, index)
    return output
    

def decode(s, n):
    lst = list(s)
    lengthS = len(lst)
    results =  [""] * lengthS
    for _ in range(lengthS):
        results = sorted([lst[i] + results[i] for i in range(lengthS)])
    return results[n]
