import math

graph={}
graph["start"]= {}
graph["start"]["1"]=6
graph["start"]["2"]=2
graph["1"]={}
graph["1"]["fin"]=1
graph["2"]={}
graph["2"]["1"]=3
graph["2"]["fin"]=5
graph["fin"]={}

infinity = math.inf
costs={}
costs["1"]=6
costs["2"]=2
costs["fin"]=infinity


parents={}
parents["1"]="start"
parents["2"]="start"
parents["fin"]=None


processed=[]

def find_lowest_cost(costs):
    lowest_cost=math.inf
    lowest_cost_node=None
    for node in costs:
        cost=costs[node]
        if cost<lowest_cost and node not in processed:
            lowest_cost=cost
            lowest_cost_node=node
    return lowest_cost_node

node =find_lowest_cost(costs)
while node is not None:
    cost =costs[node]
    neighbors=graph[node]
    for n in neighbors.keys():
        newcost=cost+neighbors[n]
        if costs[n]>newcost:
            costs[n]=newcost
            parents[n]=node
    processed.append(node)
    node=find_lowest_cost(costs)
print(costs)
print(parents)
