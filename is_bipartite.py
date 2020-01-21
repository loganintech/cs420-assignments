yes_is_bipartite = {
    "a": {"vert": ["b"], "color": None}, # red
    "b": {"vert": ["c"], "color": None}, # blue
    "c": {"vert": ["d"], "color": None}, # red
    "d": {"vert": ["e"], "color": None}, # blue
    "e": {"vert": ["f"], "color": None}, # red
    "f": {"vert": [], "color": None}, # blue
}

not_bipartite = {
    "a": {"vert": ["b"], "color": None}, # red and blue and red and...
    "b": {"vert": ["c"], "color": None}, # red and blue and red and...
    "c": {"vert": ["a"], "color": None}, # red and blue and red and...
}

def is_bipartite(v, g, parent_color):
    if g[v]["color"] is None:
        g[v]["color"] = not parent_color
    else:
        return g[v]["color"] != parent_color

    for nxt in g[v]["vert"]:
        if not is_bipartite(nxt, g, g[v]["color"]):
            return False

    return True

print(is_bipartite("a", yes_is_bipartite, True))
print(is_bipartite("a", not_bipartite, False))
