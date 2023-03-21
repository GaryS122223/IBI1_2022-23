#first we have 2 rabbits
rabbits = 2
#initialize generation counter
generation = 1

#breeding until we have at least 100 rabbits
while rabbits < 100:
#caculate the number of rabbits in different generations
rabbits = rabbits*2
#generation increase
generation = generation + 1
#output the number of generations to exceed 100 rabbits
print("generations to have at least 100 rabbits =" + str(generation))

 
