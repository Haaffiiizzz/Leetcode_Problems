numStores = int(input())
numAvailable = int(input())

itemStore = {}

for i in range(numAvailable):
    details = input().split(" ")
    store = int(details[0])
    item = details[1]  
    
    if store in itemStore:
        itemStore[store].append(item)
    else:
        itemStore[store] = [item]

numItems = int(input())
items = []

for i in range(numItems):
    items.append(input())

i = 0
paths = 0
for item in items:
    found = False
    for j in range(i, numStores):
        if item in itemStore[j]:
            found = True
            break
    i = j
    if not found:
        print("impossible")
        quit()


for key1, list1 in itemStore.items():
    for key2, list2 in itemStore.items():
        if key1 != key2 and len(list1 + list2) != len(set(list1 + list2)):
            print("ambiguous")
            quit()
print("unique")
    
    