#==============> Different data type in Python <==============================
#(1)=======================> Numerical Data type ... <=================
# Basically there are three type for store numerical task... (integer , Floating , Complex Number)

##========> integer (int)

a=10
b=5
c=-4
# print(type(a), type(b), type(c))

## output look like that <class 'int'> <class 'int'> <class 'int'>

##==========> Floating Point (float)

d=10.56
# print(type(d))

## Output tell as this is / float value 

##===========> complex Number 
# Are those number in which one path is real and other path is imaginay and in this we denote imaginary oath by ("j")

e=3+5j
# print(type(e))

## output / <class 'complex'>

#===========> TYPE CONVERSION <==============
# python Allow us to change one type to other

x=10.57
y=int(x)
z=complex(x)

# print(y) # ouput / 10
# print(z) # output / 10.57+0j



#(2) ======================> SEQUENCE TYPE (ORDER COLLECTION) <============================

# there are for mainly fout type of data type ... (str) ... (list) ...(tuple) ...(range)

# (a)=============> (str) string
# str is immutable and we only replace it ...


name="Adeel"
# print(name)
# print(name[0]) # / return first character
# print(name[2]) # /return fourth index character
# print(name[-1]) # / return last character

# # some string methode that we used 
# print(name.upper())
# print(name.lower())

# (str) is immutable : mean we can't directly make change in it instead we use .replace methode

# print(name.replace("A","j")) #/ jdeel
# print(name) # /Adeel ... we clearly seen we only replace our str variable not make properly change it our intiall value is same is it ...
# print("H"+name[1:]) # in this line of code we slice our name from one index and tehn combine in with H /Hdeel


# (b)=====================> (List) 
# list is a order squence mean (jab tak hum kud kohi change na kary wo order same rehta hai jasa hum ny define kiya hai )
# list is mutable mean we can change it but in "str" we replace it and not change the initiall value but here we change it
# List has store differnt data type together
# we use [] 

fruits = ["Apple", "Banana", "Cherry"]
# print(fruits)

# some build in methode that is used to change and update list

fruits.append("orange") # add at item at the end 
# print(fruits)
fruits.remove("Banana")
# print(fruits)
fruits.insert(0,"Adeel") # that add a element at the start of the list , first Argument show the index number and 2nd argument show the element that i added . List(index,element)
print(fruits)
fruits[0]="banana" # we can change like that also .
# print(fruits)

# we know  in list we can store ( differnt data type together)

my_list = [10, "Adeel", 3.14, True, [1, 2, 3]]

# print(type(my_list[0]))  # int
# print(type(my_list[1]))  # str
# print(type(my_list[2]))  # float
# print(type(my_list[3]))  # bool
# print(type(my_list[4]))  # list


# (c)===========> Tuple
#  basically tuple is similar to list but few changing in it.
# it immutable mean we can't change it and not change make change in it ... we can't change it's size and content
# it tuple we use parentheses


colors = ("Red", "Green", "Blue")
# print(colors)
# colors[0]="green" # by doing this we get error beacuse tuple can't allow us to make change in it ..


#(d)===============> Range 
# range is special type of data type that is used to create squence of number
r=range(1,10)
# print(list(r))

#example :
number=list(range(1,10,2))# it's mean starting from 1 , ending before the 10 and step taken 2 . 1 step is default step 
# print(number)#it's make number of list 



# (3) ======================> unsquence (unorder) data type <=================================
# Set (set)
# Dict (dict)


# =========> Set
# set is used {} bracket
# set ak unordered collect hoti hai (that mean is me element kasi fix order me store nahi hoty)
# set can't be allow duplicate number and element and it's remove duplicate number if user define duplication numbers
# it's can't be support indexing, print(myset[0]) // we get error by this 
# we add and remove items in a set

myset={10,20,30,40,50}
# print(myset) # /output {50, 20, 40, 10, 30}
nums = {1, 2, 2, 3, 4, 4,5,5,5,5, 5}
# print(nums)
nums.add(6)
nums.remove(5) # if number not found get error nums.discard(5) it's remove and can't give us error if can't found any number 
# print(nums)
nums.discard(7)
# print(nums)
# print(nums.pop()) # it's remove random number from the set
# print(nums)
# print(nums.clear()) # clear full set 
# print(nums)
b={1,6,4,8,9,10}
# print(nums|b) # union

# set also store multiple type of data but only immutable data is allow (mean jo change ho sakty wo data set me nahi a sakta )
my_set = {1, 3.14, "Hello", (5, 6)}


# in set we also apply all set property like union  , intersectiuon (&) , subtarction/difference(-) , subset (issubset()) , superset


# =============> Dict (dict)
# dict stand for dictanory
#  it's a key value pair collection 
# use {} bracket
# alway unique key duplicate key not allow 
student = {
    "name": "Adeel",
    "age": 20,
    "course": "BSCS"
}
print(student)

# access methode
# print(student["course"]) # this give us error if course is not define
# print(student.get("name")) # but by get methode we can't get error we get null and undefine value if key not found
# print(student.values()) # by this getting all the values
# print(student.keys()) #by this we get all the keys
# print(student.items()) # by this we get all key and value


# ==================> Bollen Data type <===================
# simple true and false come here 



# CONCULSION : 
# Here we learn about different concept (Data type)=> 1. Numerical data type (int , float , complex ) , 2. sequence data type (str , list , tuple , range) , 3. unsequence data type (set , dict) ,boolen data type (true , false) ...