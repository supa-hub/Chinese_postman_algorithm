from tkinter import *
import pygame
import numpy as np
import itertools

"""
Currently you can insert a graph into the algorithm by a tkinter window that is included in this code, so you do not have to code your own.
For development purposes I have bypassed this tkinter way and wrote a graph for the code to use in the algoritm.
This is because I would always have to insert the graph manually, and with alot of development it took alot of time.

If you want to use the code you will have to remove the comments over the get_the_verteces function, and remove the old, shorter one.
This can be done at lines 373, and 376.
"""

class odd_verteces_class:
    def __init__(self, lengths):
        self.length = 0

        for a_length in lengths:
            self.length += float(a_length)

    def return_length(self):
        return self.length


class indirectly_connected_paths:
    def __init__(self,  path_name, the_graph_matrix):

        # we'll use hash tables and djikstra's algorithm to solve the shortest path between the odd verteces

        start_vertex = path_name[0]
        end_vertex = path_name[1]

        self.start_vertex = start_vertex
        self.end_vertex = end_vertex

        paths_hash_map = {}
        paths_hash_map[start_vertex] = {}

        infinity = float("inf")
        the_cost_node = {}

        self.processed = []

        path_of_shortest_length = [] # the list for creating the paths name for hte shortest path

        
        for verteces in the_graph_matrix: # the start of creating the hash tables
            
            if verteces["vertex_name"] == start_vertex:  # creates the first key of the hash table by 
                for paths in verteces["paths"]:          # inserting the paths of the starting vertex
                    paths1 = paths.replace(start_vertex, "")
                    paths_hash_map[start_vertex][paths1] = verteces["paths"][paths]

        print(start_vertex, "starting vertex")
        print(end_vertex, "ending vertex")
        print(paths_hash_map, "paths_hash_map")
            
        
        for verteces1 in paths_hash_map[start_vertex]:   # adding the neighbouring paths and verteces into the hash table
            paths_hash_map[verteces1] = {}

            if verteces1 == end_vertex:
                paths_hash_map[verteces1] = {}

            else:
                for verteces2 in the_graph_matrix:
                    
                    if verteces2["vertex_name"] == verteces1:
                        for paths in verteces2["paths"]: 
                            paths1 = paths.replace(verteces1, "")
                            if paths1 == start_vertex:
                                pass
                            else:
                                paths_hash_map[verteces1][paths1] = float(verteces2["paths"][paths])

        paths_hash_map[end_vertex] = {}

        print(paths_hash_map, "paths_hash_map")

        
        for cost_name in paths_hash_map[start_vertex]:   # we create the cost table, for the length that it takes to get to each node
            the_cost_node[cost_name] = float(paths_hash_map[start_vertex][cost_name])
        
        the_cost_node[end_vertex] = infinity   # we assign the finish node a cost of infinity, because we dont know the length yet
        


        print(the_cost_node, "the_cost_node")
        

        the_parent_node = {}

        for parent_name in paths_hash_map[start_vertex]:  # we create the parent table, which will calculate the final path
            the_parent_node[parent_name] = start_vertex
        
        the_parent_node[end_vertex] = None
        
        
        node = self.find_lowest_cost_node(the_cost_node)

        while node is not None:
            cost=the_cost_node[node]
            neighbors = paths_hash_map[node]
            for n in neighbors.keys():
                new_cost = cost + neighbors[n]
                try:
                    if the_cost_node[n] > new_cost:
                        the_cost_node[n] = new_cost
                        the_parent_node[n] = node
                
                except:
                    pass

            self.processed.append(node)
            node = self.find_lowest_cost_node(the_cost_node)

        #==========================================
        checkpoint = end_vertex
        # we add the start and end point into the list before the for loop, because otherwise theyre not in the list
        path_of_shortest_length.insert(0,start_vertex) 
        path_of_shortest_length.insert(1,end_vertex)
        # -------------------------------------------

        while the_parent_node[checkpoint] != start_vertex:   # the loop for getting the paths verteces
            path_of_shortest_length.insert(1,the_parent_node[checkpoint])
            checkpoint = the_parent_node[checkpoint]
        #===========================================


        print(the_cost_node, " the last the_cost_node")
        print(the_parent_node, " the last the_parent_node")
        print(path_of_shortest_length, " the path_of_shortest_length")

        self.the_cost_node = the_cost_node
        self.path_of_shortest_length = path_of_shortest_length

        print(self.path_of_shortest_length, "the self.path_of_shortest_length")

        

              
    def find_lowest_cost_node(self, costs):
        lowest_cost = float("inf")
        lowest_cost_node = None

        for node in costs:
            cost = costs[node]
            if cost < lowest_cost and node not in self.processed:
                lowest_cost = cost
                lowest_cost_node = node

        print( "lowest_cost_node: ", lowest_cost_node)
        return lowest_cost_node


    def return_the_length(self):

        self.path_of_shortest_length1 = ""

        for x in self.path_of_shortest_length:
            self.path_of_shortest_length1 += x

        dict_of_path = []
        dict_of_path.append((self.path_of_shortest_length1,self.the_cost_node[self.end_vertex]))
        return self.path_of_shortest_length1,self.the_cost_node[self.end_vertex]

        





class chinese_postman_algorithm:
    def __init__(self):
        self.letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        self.entries = []
        self.create_vertex = []
        self.list_of_verteces = []

        self.dict_of_matrix = []    # list which we will use .copy() command 

        self.path_names = []


    def run_algorithm(self):
        #self.nparray_for_verteces = np.array()

        # --------------------------------------------------------------------------------------

        self.dict_of_matrix2 = self.dict_of_matrix.copy()    # this will hold the paths of a vertex that we will add into "self.dict_of_matrix4"

        self.dict_of_matrix4 = self.dict_of_matrix.copy()   # the dictionary that will contain a single vertex and its paths

        self.dict_of_matrix3 = []  #this will hold all of the verteces and their distances

        odd_verteces = [] # a list in which we will store every vertex that has an odd number of paths

        yy = 0

        for x in self.list_of_verteces:     #create all the verteces dictionaries
            
            yyy = 0  #variable so I get the right names to every path in the dict
            index = self.list_of_verteces.index(x)
            self.dict_of_matrix4.append(("vertex_name",self.letters[index]))
            self.dict_of_matrix4.append(("paths",""))

            for xx in x:
                path_name = sorted(self.letters[yy]+self.letters[yyy])   #these 2 lines sort the path names so they are the same at every vertex
                path_name2 = path_name[0] + path_name[1]

                self.path_names.append(path_name2)    #add the path into the list which will loop through them all


                if int(xx) == 0:  #this if block basically filters out all the paths that have a length of 0
                    pass
                else:
                    self.dict_of_matrix2.append((path_name2,xx))


                if (index+1) >= len(self.list_of_verteces):
                    pass

                yyy += 1


            print(self.dict_of_matrix2)
            print(self.dict_of_matrix4)
            self.dict_of_matrix4 = dict(self.dict_of_matrix4)
            self.dict_of_matrix4["paths"] = dict(self.dict_of_matrix2)   # add the verteces paths into the dictionary, which we will put into the dict_of_matrix3

            self.dict_of_matrix3.append(self.dict_of_matrix4)
            self.dict_of_matrix2 = self.dict_of_matrix.copy()
            self.dict_of_matrix4 = self.dict_of_matrix.copy()
                

            yy += 1

            # ------------------------------------------------------------------------------

        print(self.path_names)

        print(self.dict_of_matrix3)


        #now its time to calculate the shortest possible distance with the chinese postman algorithm
        
        for vertex in self.dict_of_matrix3:
            if (len(vertex["paths"])/2).is_integer() == False:
                odd_verteces.append(vertex["vertex_name"])

        print(odd_verteces)
        self.odd_verteces = odd_verteces

        if len(odd_verteces) == 2:
            self.get_odd_verteces_path(odd_verteces[0],odd_verteces[1])

        else:

            ranges = 0 # this variable changes so in the loop (that is next) we cycle through all the possible combinations of the verteces
            print(self.calculate_combination(len(odd_verteces)))


            perms = itertools.permutations(odd_verteces)  # we create it AGAIN, because for some reason it reset when you use the permtuations ocnce
            perms_list = list(perms)

            paths = []
            paths1 = []  # another list for when we filter out the same paths



            ranges = 0
            for perm in range(int(len(perms_list))):
                path = self.get_odd_verteces_path(perms_list[perm]) # a unique path between the odd vertices
                paths.append(path)
                ranges += 1

                [paths1.append(x) for x in paths if x not in paths1]


                
            print(paths1,"these are the paths")

                
                #vertex = vertex(self.dict_of_matrix)
                #self.new_array = np.append(self.nparray_for_verteces, vertex)

            lengths = []
            lengths1 = []

            for possible_path in paths1:  # takes 1 of the combinations from the list
                for a_path in possible_path:  # takes 1 of the paths from the combinations
                    for all_verteces in self.dict_of_matrix3:  # loop that checks if the verteces are connected, because if not then
                        if a_path in all_verteces["paths"]:   # we'll have to use djikstra's algorithm to find the shortest possible path
                            lengths.append((a_path,float(all_verteces["paths"][a_path])))
                            break
                        else:
                            indirect_path = indirectly_connected_paths(a_path, self.dict_of_matrix3)
                            lengths.append(indirect_path.return_the_length())
                            break

                    if len(lengths) == 2:    # checks if theres 2 pairs of odd vertices, if there is,then get the unique paths
                        print("JOOOOOORARARAR")  
                        #unique_paths = odd_verteces_class(lengths)
                        lengths1.append(dict(tuple(lengths.copy())))
                        lengths.clear()

                        #print(unique_paths.return_length())
                        print(lengths1)



            print(lengths)
        

        
        #this is the part which calculates the total length
        for paths_lengths in self.dict_of_matrix3:
            for a_path_length in paths_lengths["paths"]:
                print(a_path_length)

        
    def get_odd_verteces_path(self,permutation):
        length = int(len(self.odd_verteces)/2)

        list_of_twos = []

        for i in range(length):
            list_of_twos.append(2)

        input_ = iter(permutation)
        gg = [list(itertools.islice(input_,2)) for lem in list_of_twos]

        gg2 = []

        for gg1 in gg:
            gg2.append(sorted(gg1))

        gg3 = []

        for paths in gg2:
            paths2 = paths[0] + paths[1]
            array = np.array(paths)
            gg3.append(paths2)

        
        

        #print(gg)
        #print(gg2,"juu")
        #print(gg3,"eii")

        return gg3

    


    def calculate_combination(self,odd_vertex_count):
        combination_value_1 = 1
        combination_value_2 = 1
        for x in range(odd_vertex_count):
            combination_value_1 = combination_value_1*(x+1)

        for x in range(odd_vertex_count-2):
            combination_value_2 = combination_value_2*(x+1)

        print(combination_value_1)
        print(combination_value_2)
        combination_value = combination_value_1/(2*combination_value_2)

        return combination_value

    def get_the_verteces(self):
        self.list_of_verteces = [['0', '0', '34', '54', '765'], ['234', '0', '54', '23', '0'], ['543', '45', '0', '0', '365'], ['567', '65', '45', '0', '0'], ['67', '0', '678', '987', '0']]
        self.run_algorithm()
        """        
    def get_the_verteces(self):

        count = 0
        self.create_vertex2 = self.create_vertex.copy() # I have to copy so the code works

        for entries1 in self.entries: #loops in the textentries so it gets all the text
            the_verteces = entries1.get()
            self.create_vertex2.append(the_verteces) 
            
            print(entries1.get())

            count += 1

            if count == int(self.num_of_verteces):
                self.list_of_verteces.append(self.create_vertex2)     #makes the list that will be inserted into the matrix
                self.create_vertex2 = self.create_vertex.copy()
                count = 0

            

            print(self.list_of_verteces)
        
        self.matrix = np.array(self.list_of_verteces)   #create the matrix for use in the algorithm
        print(self.matrix, "joo")
        print(self.matrix[0, :],"JUUUUU")


        #self.run_algorithm()

"""




    def get_the_num_of_verteces(self):
        global textentry
        global window
        self.num_of_verteces = textentry.get()
        print(self.num_of_verteces)
        window = Tk()
        window.title("chinese_postman")

        for x in range(int(self.num_of_verteces)):      #the loops for the entries
            for z in range(int(self.num_of_verteces)): 
                self.textentry1 = Entry(window, width=20, bg="white")         # entry for the lengths of the verteces
                self.textentry1.grid(row=(z+1), column=x, sticky=W)        #locates the next entry into position
                self.entries.append(self.textentry1)            #makes a list of all the entries so you get all the distances between

            Label(window, text=self.letters[x], bg="white", fg="black", font="none 10 bold") .grid(row=0, column=x, sticky=W) #give all of the columns the name of the vertex


 

            
        Button(window, text="insert the verteces", width=20, command=lambda: self.get_the_verteces()) .grid(row=(int(self.num_of_verteces)+1), column=(int(self.num_of_verteces)-1), sticky=W)
        
        #the button to insert the verteces into the algorithm part


        window.mainloop()




the_algorithm_class = chinese_postman_algorithm()

window = Tk()
window.title("chinese_postman")

textentry = Entry(window, width=20, bg="white")  #entry on how many verteces
textentry.grid(row=2, column=0, sticky=W)

Button(window, text="num of verteces", width=20, command=the_algorithm_class.get_the_num_of_verteces) .grid(row=3, column=0, sticky=W)

window.mainloop()