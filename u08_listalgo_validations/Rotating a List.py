queue = ["Person1", "Person2", "Person3", "Person4", "Person5"]
rotate = int(input("How may time to roate? : "))
person = queue[0]
for i in range(rotate+1):
    queue.remove(person)
    queue.insert(i,person)
print(queue)