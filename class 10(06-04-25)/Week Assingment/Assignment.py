# ==================> You are NOT allowed to use: (List comprehension) & (Loops (for, while)) <======================


'''
1. Create and Initialize Superhero List:
Start by creating the list of superheroes as shown above. You can add new superheroes by asking the
user for their details.

'''


superheroes = [
("Superman", 85, "DC", 4.0),
("Iron Man", 100, "Marvel", 5.0),
("Wonder Woman", 90, "DC", 4.9),
("Hulk", 95, "Marvel", 4.8),
("Thor",95,"Marvel",4.9),
("wolverine",70,"DC",3.0),
("Captain America",65,"Marvel",3.2),
]

print(superheroes)






a,b,c,d,e,f,g=superheroes



'''
2. Filter Superheroes by Power Level:
Find the super heroes with maximum power level and display them.

'''
def powerlevel(item):
    return item[1]

filterByPowerLevel=sorted(superheroes,key=powerlevel,reverse=True)[:1][0]
# print('\n',f'Super Hero which have maximum Power level :  "{filterByPowerLevel[0]}"\n Power level: {filterByPowerLevel[1]}')




'''
3. Sort Superheroes by Rating:
Use the sorted() function to sort the superheroes by their rating in descending order and display
them.

'''

def filt(item):
    return item[-1]

sortheroByrating=sorted(superheroes,key=filt,reverse=False)
# print(sortheroByrating)



'''
4. Calculate Team Statistics:
Calculate and display the total power level and the average rating of the superheroes in the filtered
team.

'''

sumofrating=a[-1],b[-1],c[-1],d[-1],e[-1],f[-1],g[-1]
# print('Averge rating out 5.0: ',round(sum(sumofrating)/len(sumofrating),1))





'''
5. Remove a Superhero:
Ask the user to enter a superhero name to remove from the list. Manually search for the superhero by
name and remove it from the list.

'''


print("\n============> you want to remove a Superhero  <===============")
print("We have Super Hero's List:\n", superheroes)
response = input("\nYes or No? Just type e.g., y/n: ")

if response.lower() == 'y':
    removeHero = input("Just Type Hero Name: ")

    # Recursive function to remove a superhero (witout Loop and List List comprehension)
    def remove_superhero(lst, name, index=0):
        if index >= len(lst):  
            return lst  
        if lst[index][0] == name:  
            return lst[:index] + lst[index+1:] 
        return remove_superhero(lst, name, index + 1)  

    superheroes = remove_superhero(superheroes, removeHero)

print("\nUpdated Superhero List:\n", superheroes)




'''
6. Add a New Superhero:
Ask the user for the superhero's name, power level, universe, and rating and add that superhero to the
list. (One super hero is to be taken from user)
Example input:
 Name: Flash
 Power Level: 80
 Universe: DC
 Rating: 4.6

'''


addYourSuperHero=str(input("Enter SuperHero Name first: ")),int(input('Power Level out of 100: ')),str(input("Universe: ")),float(input("Rating for your superHero out of 5.0: "))

print(addYourSuperHero)
superheroes.append(addYourSuperHero)
print(superheroes)





'''
7. Display the Final Team:
After filtering, sorting, and removing superheroes, display the final list of superheroes along with their
details.

'''

print("finilized SUperHero list : ", superheroes)





'''
8. Set Operations on Superheroes:
Perform the following operations using a set:
- Create a set of unique superhero names.
- Add the newly added superhero to the set.
- Check for a specific superhero membership (e.g., "Flash").
- Display the final set of superheroes.
'''

# Creating a set of unique superhero names
superhero_set = set(superheroes)

# Adding the newly added superhero to the set
superhero_set.add(addYourSuperHero[0])

# Checking for membership of 'Flash'

flash_exists = "Flash" in superhero_set


print(f"\nIs Flash in the superhero set? {flash_exists}")

# Displaying the set of superheroes
print("\nFinal Set of Unique Superheroes:", superhero_set)