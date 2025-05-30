# =====================> third class <========================
# variable in python is refernce not the container .. (learn more)
'''
one variable has three property , identity (addreas where variable lies in memory ) , type (datatype) and value (it's value of the varible)
for tommorrow gol laearn about how and where the identity is used ,

'''
# 
# dir() in python is used that tell all the variable and stuff that we define and all other function and alll other stuff comes in this  basically (when we check some type data and type of this then we used dir() for example if i have a list then by then dir () methode we found all the methode that we used and assign we also assign this in set and on differnt )
my_list = [1, 2, 3]
# print(dir(my_list))


my_set={1,2,3,4,5,6}
print(dir(my_set))

''' the output i get is this .... by this print(dir(my_set))
['__and__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']
'''
x=(0==False)
print(x)
c=(0==False
   )

# why in division 2/4 become float value  ( resolve this formate problems  jal)

x=4/2 
# print(type(x)) # why this get float value 


#=====================> Type of Division <=====================
# true division
# float division
# ====================> true division
# it's is denoted by "/" singal in this type we also get float type answer
x1=4/2 
print(type(x1))


#==============> float division
# in which we always get int , it's denoted by //
x2=4//2
print(type(x2))

