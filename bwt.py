def encode(s):
    results = []
    lst = list(s)
    for _ in range(len(lst)):  # rotate once for each element
        lst.insert(0, lst.pop())  # remove last item and insert at front
        results.append("".join(lst))  # append a *copy* so future changes don't overwrite
    results = sorted(results)
    lastCol = ""
    index = None
    for i, r in enumerate(results):
        lastCol += results[i][-1]
        if r == s:
            index = i
    output = (lastCol, index)
    return output
    

def decode(s, n):
    if not s:
        return ""
    lst = list(s)
    lengthS = len(lst)
    results =  [""] * lengthS
    for _ in range(lengthS):
        results = sorted([lst[i] + results[i] for i in range(lengthS)])
    return results[n]

# ### Top Community Solution
# def encode(s):
#     lst = sorted( s[i or len(s):] + s[:i or len(s)] for i in reversed(range(len(s))) )
#     return ''.join(ss[-1] for ss in lst), s and lst.index(s) or 0

# def decode(s, n):
#     out, lst = [], sorted((c,i) for i,c in enumerate(s))
#     for _ in range(len(s)):
#         c,n = lst[n]
#         out.append(c)
#     return ''.join(out)
# note the use of slicing to handle rotation
# also list comprehension
