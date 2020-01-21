graph = {
    "a": ["b", "c"],
    "b": ["d", "e"],
    "c": ["d"],
    "d": [],
    "e": []
}

list = []

def top_sort(v, g):
    for e in g[v]:
        top_sort(e, g)

    if v not in list:
        list.append(v)

top_sort("a", graph)
list.reverse()
print(list)
