from collections import deque
def main():
    if bfs("you"):
        print('True')
    else:
        print("there is no mango seller in the graph")
#graph implementation
graph = {}
graph["you"] = ["asem", "ali", "ahmed"]
graph["asem"] = ["abood", "anas"]
graph["ali"] = ["kardsh"]
graph["ahmed"] = ["noor", "eslam", "reda"]
graph["abood"] = ["amer"]
graph["anas"] = []
graph["kardsh"] = []
graph["noor"] = []
graph["eslam"] = []
graph["reda"] = ["the only and the 1"]
graph["amer"] = []
graph["the only and the 1"] = []


#check who is the mango seller
def is_a_mango_seller(person):
    if person[-1] == "1":
        return True
    else:
        return False
#BFS Function
def bfs (name):
    search = deque()
    search += graph[name]
    searched = []
    while search:
        person = search.popleft()
        if not person in searched:#check visited or not
            if is_a_mango_seller(person):
                print(person + " is a mango seller")
                return True
            else:
                search += graph[person]#add the person to the deque
                searched.append(person)
    return False
main()

