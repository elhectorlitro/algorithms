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
   visited = []
   queue.append(dep)#You add the departing node as the first on the queue
   while queue: #Until the queue gets empty 
     key = queue.pop() #pop the queue
     print("current key: " + key)
     node = gra[key]
     print("Tried with: "+str(node))
     if Contains(node, obj) : 
          print("Found a way to the node")
          return True
     else :
          visited.append(key)
          for each_key in node:
             print("Checking: " + each_key)
             if (Check(visited,each_key)) :
                  print(str(each_key)+" already visited")
             else :
                  print(str(each_key)+" not visited yet")
                  queue.append(each_key)#If it does not contain, a path to the objective, add the node to the queue
                  print(str(each_key)+" appended")
   return False

def Contains(node, obj):
     if obj in node:
       print(str(obj)+" contained") 
       return True
     else : 
       return False

def Check(Visited,key):
    if key in Visited:
       return True
    else :
       return False
print("Type the node you want to departure from: ")
departure = str(input())
print("Type the node you want to reach to: ")
objective = str(input())
print(BreadthFirstSearch(graph,departure,objective))

