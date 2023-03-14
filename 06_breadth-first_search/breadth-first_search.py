from collections import deque

# Verify if the persons name ends with an m, if ends, the person sels mango
def person_is_seller(name):
    return name[-1] == 'm'


graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

def search(name):
    # Creates a double ended queu
    search_queue = deque()
    search_queue += [name]
    # In this way you can keep track of which people you've searched before
    searched = set()
    while search_queue:
        person = search_queue.popleft()
        # Only search if the person haven't already been searched
        if person in searched:
            continue
        if person_is_seller(person):
            print(person + " is a mango seller!")
            return True
        search_queue += graph[person]
        # Marks the person as searched
        searched.add(person)
    return False
search("you")
