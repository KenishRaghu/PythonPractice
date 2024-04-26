collection = {1,2,3,4,5,"hello",2}
print(collection)

print(len(collection))

empty_collection = set() # Empty collection
print(empty_collection)

collection.add("World")
print(collection)

collection.pop()
print(collection)

#Adding 2 sets
set1 = {1,2,3}
set2 = {2,3,4}

set1 = set1.union(set2)

print(set1)

set1 = set1.intersection(set2)
print(set1)