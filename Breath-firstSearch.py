import random 
import collections 

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

def BreadthFirstSearch(gra, dep, obj):#You give the graph, element you're departuring from and the node that is your objective
   queue = []#Creates a new queue
   queue.append(gra[dep])#You add the departing node as the first on the queue
   while queue: #Until the queue gets empty 
     node = queue.pop() #pop the queue
     if Contains(node, obj) : 
          print("Found a way to the node")
          return True
     else : 
          queue.append(gra["node"])#If it does not contain, a path to the objective, add the node to the queue
   return False

def Contains(node, obj):
     if obj in node:
         print(str(obj)+" contained") 
         return True
     else : return False

print(BreadthFirstSearch(graph,"origin","a"))

