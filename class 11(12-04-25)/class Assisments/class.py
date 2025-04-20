'''
Today's we learn about dictionaly in python ,,, in (python) dictionaly is work and sytax like a object in javascript . 

1) Dictionary is basically is a mutable data type in python ..

2) it's starting with {} bracket is work like a {name:"adeeel", age : 34} that store in key and value , 

3) key must be unique always we repaeat value but can reapt key 

4) it's is heterogrnous type () it's both mutable and imutable .. 

5) dictionary is use when we want to store big data and example together 

'''

dic1={"name":"Adeel","age":20 }
print(dic1)
print(type(dic1))

# this give us help hoe dictionary work ( agr mojy kasi function par kuch help chaye to i simply type the name help that is build in function  )

# help(dic1)






#1) create a simple dictionary

dic1a={"name":"Adeel","age":20,"name":"SanaUllah","age":22}
print(dic1a)
# here in above code not get {error} but here is the issue it's will only return last name and age beause we only pas unique key ...

dic2={"myname":"Adeel","age":20,"student2nd":"SanaUllah","age2":22}
print(dic2) 

#  2) other way to create a dictionary 

dic3=dict(name="dict3" , age=45)
print('dict3 :',dic3)



# 3) let create a list and pas tuples they act like a dictionary
dic4=dict ([("name","Adeel"),("Age", 47)])
print(dic4)


'''
key always string , tuple and number beacuse this is imutable beacuse key must imutable beacuse it's a identi
'''


# ====================> nested dictionary <==============

dict5={
    'name':'Adeel',
    'age':56,
    'addreas':{"city":"lahore",'PostAddress':{'street':'street45 Lahore','housenumber':79, 'postcode':7890} ,"Country":"pakistan"},
    'number':'0300-000000'
}
print('\n',dict5)




# convert list into dictionary 
# list1=[1,2,3,4,5]
# a,b,c,d,e=list1
# print(tuple(a,b,c,d,e))



# create 

dic6={
    'name':{
        'first_name':"Adeel",
        'last_name':'Ashraf'
    },
    'friend':{
        'first_name':'Sanaullah',
        'last_name':'Ismail'
    },
    'parents':{
        'mother':"Halima",
        'father':'Ashraf',
    },
    'sibling':{
        'brother':'Naveed',
        'Sister':'Rehana'
    },
}

print(dic6)



''' 
Question # 1 ) list is order squence so why not we access this by index number?
Answer = is that dictionary currenty not allow us to access the dictionarty by indexs number ? they allow us  to access the dictionary by key vlaue pair

below we done this by 
dictionry name and pair 

'''
# methode 1 (this methode is also good but when i access a undefined key like name1 which is not availble in dictionary then i get a error)
print(dic6['name'])
print(dic6['name']['last_name'])

# methode 2 ( by this methode i can't get any error if key is not availble in dictionary )


print(dic6.get('friend'))


# Methode 3 (if we have a requiremen to access the the dictionary by index number what should we do )?
# if we want to find and access the item by index number we just type caste diuctionary in to list and found data by index numbers


print('\n===============> M(3) convert Nested dictionary in to List <=====================')
dict_into_list=list(dic6.items())
# basically this .items() return a tuple and then i convert this in to list and then indexing we directry index in tuple 
print('\n Just convert dict_into_list : \n',dict_into_list) 








"""
if we have two  dictionary with same name and same key and value then tell it's id is same or not ?

Ans=> it's id is not same in dictionary ,, dictionar
"""


dic7={
    'name':'Adeel',
    'age':78
}
print(dic7.get('name'))
print(dic7.get('age'))




# create a car dictionary 
print('\n==================> create a Car dictionary <==========================')
car={
    "car-Brand":"Audi",
    "Model":25,
    'Manufactual_date':'04-04-25'
}
print(car['car-Brand'])
print(car['Model'])
print(car['Manufactual_date'])


print('====> by get method <=====')
print(car.get('car-Brand').upper())
print(car.get('Model'))
print(car.get('Manufactual_date'))




print('\n=====> try item methode <=====')

li=(car.items())
print(type(li))
print(li)
li2=(car.keys())
print(type(li2))
print(li2)
li3=(car.values())
print(type(li3))
# print(li3[0]) # question arrise here ? we can use like that beacuse currently it's type is not the tuple is the dict now we want to access specific value then i first convert it type currently its type is : dict_key , dic_value , dic_items  and now i translate this in to list



print('\n=====> Adding and modify <=====')


my_info={
    "name":"Audi",
    "city":"LAHORE",
    'Address':'upper mall',
    'age':40
}
my_info['Address']='TUrkey'
print('update age',my_info)


dicitem=my_info.items()
print(type(dicitem))





# update value 
# di.update({'ker':"value2"})


# by this we update one dictionarya and add to other dictioanry d1.update(d2)





# removing dictionary
# del d1[key]
print('\n=====> remove Specific key pair <======')
print('Actuall Dictonary :\n',my_info)
del my_info['age']
print('After Delete Age key :\n ',my_info)


# del(wholr dictionay)



# we also use popitem() in to pop some thing


print('\n=====> we also use Pop methode <======')

# d1.popitem();

'''
Actually Popitem() methode remove last element by LIFO methode , is me hum kohi key value pas nahi karta agr asa kary gy to ya error dy ga beacuse ya methode is liy bana hai k ya automatically remove the last item
'''
my_info.popitem()
print('After applying Popitem : ',my_info)
my_info.pop('city') # the alway need a argument 
print("After applying pop('city')",my_info)


# d1.pop(here we pass the key) so that inly 


# d1.clear() remove all items from dictoonay  but it return "none" d1={}


# sorting function

'''
sorted function always return a lsit 

'''



print('\n===> Learn about Sorted Funtion <====')

'''
in sorted function they sorted(itratar,key,reverse) 
'''

def sortitem(item):
    key,values=item
    if key == 'Model':
        return values
    else:
        return float('inf')
        

print(car)
sortDic=sorted(car.items(),key=sortitem)
print('sorted dic :\n',sortDic)



'''
branching is in if and else 
'''
