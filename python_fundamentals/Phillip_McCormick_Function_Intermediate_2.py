#1
x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

# How would you change the value 10 in x to 15?  Once you're done x should then be [ [5,2,3], [15,8,9] ].  
x[1][0]=10
print(x)

#How would you change the last_name of the first student from 'Jordan' to "Bryant"?
sports_directory['basketball'][1]='Bryant'
print(sports_directory)

#For the sports_directory, how would you change 'Messi' to 'Andres'?
sports_directory['soccer'][0]='Andres'
print(sports_directory)

# For z, how would you change the value 20 to 30?
z[0]['y']=30
print(z)

#2 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

def iterateDictionary(students): 
    for i in range(len(students)):
        print(students[i])

#3 Create a function that given a list of dictionaries and a key name, it outputs the value stored in that key for each dictionary.  For example, iterateDictionary2('first_name', students) should output
def iterateDictionary2(key, list): 
    for i in range(len(list)):
        print(students[i][key])
iterateDictionary2('first_name',[
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
])

#4 Create a function that prints the name of each location and also how many locations the Dojo currently has.  Have the function also print the name of each instructor and how many instructors the Dojo currently has.  For example, printDojoInfo(dojo) should output
def locationsInstructions(dojo):
    for i in dojo:
        print(len(dojo[i]),i)
        for x in range(len(dojo[i])):
            print(dojo[i][x])
locationsInstructions({
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
})


