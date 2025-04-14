from collections import *
dic = {
    1 : set([2,3]),
    2 : set([3,4,5]),
    3 : set([4,5,6]),
    4 : set([5,6]),
    5 : set([6]),
    6 : set([])
}



def findParent(dic,child):
    parent = set()
    start = deque([child])
    reverse = defaultdict(set)
    for key in dic:
        for value in dic[key]:
            reverse[value].add(key)
    while (start):
        node = start.popleft()
        for key in reverse.get(node,[]):
            if key not in parent:
                parent.add(key)
                start.append(key)
    return parent
print(findParent(dic,4))
def findNeighbour(dic,child):
    nodes = dic.get(child, [])
    directNodes = findParent(dic,child)
    all = set(list(nodes) + list(directNodes))
    return all
print(findNeighbour(dic,5))


#  hill climbing (variante)
# simulated Annealing