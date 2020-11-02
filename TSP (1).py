import matplotlib.pyplot as plt

#Since our problem has 5 cities, so five lists(arrays) with corresponding cities and distances
#like in m1 we have ludhiana at 0,0 and in m2 we have jalandhar at 0,0 ...
m1 = [[0,61,140,106,93],[61,0,80,149,154],[140,80,0,229,235],[106,149,229,0,75],[93,154,235,75,0]]
m2 = [[0,61,80,149,154],[61,0,140,106,93],[80,140,0,229,235],[149,106,229,0,75],[154,93,235,75,0]]
m3 = [[0,140,80,229,235],[140,0,61,106,93],[80,61,0,149,154],[229,106,149,0,75],[235,93,154,75,0]]
m4 = [[0,106,149,229,75],[106,0,61,140,93],[149,61,0,140,154],[229,140,80,0,235],[75,93,154,235,0]]
m5 = [[0,93,154,235,75],[93,0,61,140,106],[154,61,0,80,149],[235,140,80,0,229],[75,106,149,229,0]]
#Storing the cities and there respective lists in a dictionary, helps in calling their respective TSP function
choice = {"1":[m1,0],"2":[m2,1],"3":[m3,2],"4":[m4,3],"5":[m5,4]}
# storing the cities as per their matrix mentioned above for printing at last the path
cities = [["Ludhiana","Jalandhar","Amritsar","Chandigarh","Patiala"],    #m1
          ["Jalandhar","Ludhiana","Amritsar","Chandigarh","Patiala"],    #m2
          ["Amritsar","Ludhiana","Jalandhar","Chandigarh","Patiala"],    #m3
          ["Chandigarh","Ludhiana","Jalandhar","Amritsar","Patiala"],    #m4
          ["Patiala","Ludhiana","Jalandhar","Amritsar","Chandigarh"]]    #m5

# the TSP method where the shortest path and the distance is being calculated,
# it takes matrix as argument in which it performs the operations
ch = 'y'
while(ch != 'n'):
    lis1 = []
    def TSP(m,cities):
        lis = []
        distance = m; # storing the matrix in distance for further  ...

        # method to calculate length of the path ..
        def path_length(path):
            return sum(distance[i][j] for i, j in zip(path, path[1:]))

        # Storing the set of all the cities to be visited ....
        next_city = set(range(len(distance)))

        # Current state {(positon, visited_position): shortest_path}
        state = {(i, frozenset([0, i])): [0, i] for i in range(1, len(distance[0]))}

        for i in range(len(distance) - 2):
            next_state = {}
            for position, path in state.items():
                current_position, visited = position

            # Checking all nodes that have not been visited till now ...
                for node in next_city - visited:
                    new_path = path + [node]
                    new_position = (node, frozenset(new_path))

                    # Updating the new_state if (current position, visited position) is not in next state or we found shorter path
                    if new_position not in next_state or path_length(new_path) < path_length(next_state[new_position]):
                        next_state[new_position] = new_path

            state = next_state

    # Finding the shortest path from possibilities
        shortest = min((path + [0] for path in state.values()), key=path_length)
        print("\n\tThe shortest distance is : "+str(path_length(shortest))+" KM")
        print("\n\tThe path followed is : \n")
        lis.append(cities[choice[city][1]][0])
        print("\t"+cities[choice[city][1]][0],end="")
        for x in shortest[1:]:
            print("---->",end="")
            lis.append(cities[choice[city][1]][x])
            print(cities[choice[city][1]][x],end="")
        print("\n\n\tAlso : \n\n")
        print("\t"+cities[choice[city][1]][0],end="")
        shortest.pop()
        for x in shortest[::-1]:
            print("---->",end="")
            print(cities[choice[city][1]][x],end="")
        return lis

    print("\n\tHello!!! welcome to the Tavelling Salesman Problem !!!!! \n\tHere are the cities name ... ")
    print("\n\t1.Ludhiana   2.Jalandhar   3.Amritsar  4.Chandigarh   5.Patiala \n")
    city = input("\tEnter the starting city number : ")

# Calling the respective TSP function using the dictionary choice as mentioned above  ..
    lis1 = TSP(choice[city][0],cities)

#The graph has fixed vertices but as per the user choice the labels of these vertices changes ...
    x =(choice[city][0])[0]     #5[0,61,140,106,93,0]
    y = (choice[city][0])[4]   #5[0,93,154,235,75,0]
    x.append(0)
    y.insert(0,0)
# corresponding y axis values
    fig= plt.figure(figsize=(10,6))
    for i in range(6):
        plt.plot(x[i],y[i],marker = 'o',markersize=10)
        plt.annotate(lis1[i],(x[i],y[i]),size=15)
    plt.plot(x,y,linestyle = '-.')
    plt.title("\nThe graph of the shortest path when the starting city is " + lis1[0],fontsize=18)
    plt.xlabel('Distance in KM',fontsize=15)
    plt.ylabel('Distance in KM',fontsize=15)
    plt.xlim(0, 300)
    plt.ylim(0, 300)
    plt.show()
    ch = input("\nWant to find path for other city? (enter y for yes and n for no)").casefold()
    print("\n\n\n")
