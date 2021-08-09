import random 
import queue 

graph = {}
graph["origin"] = ["a", "b", "c", "d", "e", "f"]
graph["a"] = ["origin", "h"]
graph["b"] = ["origin", "i", "j", "k", "v"]
graph["c"] = ["origin", "m"]
graph["d"] = ["origin", "n", "o"]
graph["e"] = ["origin","o"]
graph["f"] = ["origin"]
graph["g"] = ["h", "p"]
graph["h"] = ["a", "r"]
graph["g"] = ["h", "p"]         
graph["h"] = ["a", "r", "g"]
graph["i"] = ["b"]
graph["j"] = ["b"]
graph["k"] = ["b","s", "t", "l"]
graph["l"] = ["k"]
graph["m"] = ["c", "u", "v"]
graph["n"] = ["d", "w"]
graph["o"] = ["d", "x","e"]
graph["p"] = ["g","x"]
graph["q"] = ["r","z"]
graph["r"] = ["q", "h"]
graph["s"] = ["k"]
graph["t"] = ["k"]
graph["u"] = ["m"]
graph["v"] = ["m"]
graph["w"] = ["n"]
graph["x"] = ["o", "p"]
graph["y"] = ["z"]
graph["z"] = ["y"]

def BreadthFirstSearch(gra, dep, obj):#You give the graph, element you're departuring from and the node that is your objective
   q = queue.Queue()#Creates a new queue
   visited = []
   q.put(dep)#You add the departing node as the first on the queue
   while not q.empty(): #Until the queue gets empty 
     key = q.get() #pop the queue    
     node = gra[key]
     if Check(node, obj) : 
          print("Found a way to the node")
          print("Node visited: {}".format(visited))
          return True
     else :
          visited.append(key)
          for each_key in node:
             if (Check(visited,each_key))==False :#If it is not on the visited record append it
                q.put(each_key)#If it does not contain, a path to the objective, add the node to the queue
   return False

def Check(node,key):
    if key in node:
       return True
    else :
       return False

print("Type the node you want to departure from: ")
departure = str(input())
print("Type the node you want to reach to: ")
objective = str(input())
print(BreadthFirstSearch(graph,departure,objective))

