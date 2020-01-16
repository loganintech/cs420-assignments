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
    # print(v, parent_color)
    # print(g)
    if g[v]["color"] is None:
        if parent_color == "red":
            g[v]["color"] = "blue"
        else:
            g[v]["color"] = "red"
    else:
        return g[v]["color"] != parent_color

    for nxt in g[v]["vert"]:
        if not is_bipartite(nxt, g, g[v]["color"]):
            return False

    return True

print(is_bipartite("a", yes_is_bipartite, "red"))
print(is_bipartite("a", not_bipartite, "blue"))
