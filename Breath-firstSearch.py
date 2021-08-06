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
graph["h"] = ["a", "r", "g"]
graph["i"] = ["b"]
graph["j"] = ["b"]
graph["k"] = ["b","s", "t", "l"]
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
   visited = []
   way = []
   queue.append(dep)#You add the departing node as the first on the queue
   while queue: #Until the queue gets empty 
     key = queue.pop() #pop the queue    
     node = gra[key]
     way.append(key)    
     if Check(node, obj) : 
          way.append(obj)
          print("Found a way to the node")
          print("way: ")
          print(way)
          print("Visited: ")
          print(visited)
          return True
     else :
          visited.append(key)
          way = CheckPath(visited, way, key, gra)
          for each_key in node:
             if (Check(visited,each_key))==False :#If it is not on the visited record append it
                queue.append(each_key)#If it does not contain, a path to the objective, add the node to the queue
   return False

def Check(node,key):
    if key in node:
       return True
    else :
       return False

def CheckPath(Visited, Way, Key, Gra) : 
    check = all(item in Visited for item in Gra[Key])
    if check is False :
       return Way
    else : 
       return CheckPath(Visited, Way[:Way.index(Key)],Way[Way.index(Key)-1],Gra)

print("Type the node you want to departure from: ")
departure = str(input())
print("Type the node you want to reach to: ")
objective = str(input())
print(BreadthFirstSearch(graph,departure,objective))

