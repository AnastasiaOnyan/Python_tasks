#add two vectors using their coordinates

data = []
answer = 0

for x in range(2):
    for x in input("Enter vectors coordinates separated by spaces: ").split("\n"):
        data.append(x.split(" "))

vect_dimension = 0

for i in data[0]:
    vect_dimension += 1

for j in range(vect_dimension):
    answer += int(data[0][j]) * int(data[1][j])
    
print(answer)
    


    


