import random 


graph = {}
graph["origin"] = ["a", "b", "c", "d", "e", "f"]
graph["a"] = ["origin", "h"]
graph["b"] = ["origin", "i", "j", "k"]
graph["c"] = ["origin", "m"]
graph["d"] = ["origin", "n", "o"]
graph["e"] = ["origin"]
graph["f"] = ["origin"]
graph["g"] = ["h", "p"]
graph["h"] = ["a", "r"]
graph["g"] = ["h", "p"]         
graph["h"] = ["a", "r"]
graph["i"] = ["b"]
graph["j"] = ["b"]
graph["k"] = ["s", "t", "l"]
graph["l"] = ["k"]
graph["m"] = ["c", "u", "v"]
graph["n"] = ["d", "w"]
graph["o"] = ["d", "x"]
graph["p"] = ["g"]
graph["q"] = ["r"]
graph["r"] = ["q", "h"]
graph["s"] = ["k"]
graph["t"] = ["k"]
graph["u"] = ["m"]
graph["v"] = ["m"]
graph["w"] = ["n"]
graph["x"] = ["o"]
graph["y"] = ["z"]
graph["z"] = ["y"]

def BreadthFirstSearch():
   return 0

