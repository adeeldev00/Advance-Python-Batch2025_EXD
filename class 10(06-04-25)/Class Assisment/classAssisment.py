#=================> class assignment <======================


travel_countries=(
    ("japan",7),
    ("anatartika",5),
    ("uk",6),
    ("London",4),
    ("Iran",3),
    ("Sham",10),
    ("Turkey",15),
    ("Istanbol",14),
    ("pakistan",12),
    ("Aust",2),
)

# 1. total trip duaration

days=(
    travel_countries[0][1],
    travel_countries[1][1],
    travel_countries[2][1],
    travel_countries[3][1],
    travel_countries[4][1],
    travel_countries[5][1],
    travel_countries[6][1],
    travel_countries[7][1],
    travel_countries[8][1],
    travel_countries[9][1],)



print(f'total numbers of trip durations days: {sum(days)} days')


# 2. Found middle number 

middleCountry=(len(travel_countries)//2)
print("middle country and days:",travel_countries[middleCountry-1])



# 3. Extarct All country name not the day
countryname=(
    travel_countries[0][0],
    travel_countries[1][0],
    travel_countries[2][0],
    travel_countries[3][0],
    travel_countries[4][0],
    travel_countries[5][0],
    travel_countries[6][0],
    travel_countries[7][0],
    travel_countries[8][0],
    travel_countries[9][0],)


 
print('Only country name:',countryname)




# 4. check if country found or not 
print("india" in countryname)




# 5. find top three longest stay

def getday(item):
    return item[1]

top_3=sorted(travel_countries,key=getday,reverse=True)[:3]

print("top 3 longest stay",top_3)


# 6 change the uk with Greece

temp1=travel_countries[:2]
temp2=travel_countries[3:]
temp3=("Greece",6)



replace_country=temp1+(temp3)+temp2
print(temp1)
print(temp2)
print(type(temp3))
print(type(temp2))
print(type(temp1))


print(replace_country)
