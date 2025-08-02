with open("shapes.txt","r") as f:
    shape = f.read()
with open("colours.txt","r") as f:
    colour = f.read()
for i in range(7):
    data_store = {}
    data_store[shape] = colour
print(data_store) 


# A text file shapes.txt stores a list of shapes with a comma between each value.  

# The current contents of shapes.txt are: 
# star,sphere,square,triangle 

# A text file colours.txt stores a list of colours with a comma between each value.  

# The current contents of colours.txt are: 
# red,yellow,green,blue 

# A program reads the data from each file and creates a dictionary of the values 
# so that each shape has an associated colour. 
# The first value in each file will be joined, for example, star and red. 

# The data is stored in a global dictionary with the identifier data_stored. 