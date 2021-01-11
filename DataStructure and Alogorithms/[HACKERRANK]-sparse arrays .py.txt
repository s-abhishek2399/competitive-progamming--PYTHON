strings_count = int(input())

strings = []

for _ in range(strings_count):
    strings_item = input()
    strings.append(strings_item)

queries_count = int(input())

queries = []

for _ in range(queries_count):
    queries_item = input()
    queries.append(queries_item)

z=[]
for i in queries:
    if i in strings:
        z.append(strings.count(i))
    else:
        z.append(0)
print(*z, sep = "\n") 
