# Sequence Types
#Note: use print() to execute the examples. Comment out examples after they've been demoed.

# Creating Lists
#1. ✅ Create a list of 10 pet names
pet_names = ['Rose', 'Meow Meow Beans', 'Mr.Legumes', 'Luke', 'Lea', 'Princess Grace', 'Spot', 'Tom', 'Mini', 'Paul']

# Reading Information From Lists
#2. ✅ Return the first pet name 
# print(pet_names[0])

#3. ✅ Return all pet names beginning from the 3rd index
# print(pet_names[2:])

#4. ✅ Return all pet names before the 3rd index
# print(pet_names[:2])

#5. ✅  Return all pet names beginning from the 3rd index and up to the 7th
# print(pet_names[2:7])

#6. ✅ Find the index of a given element
# print(pet_names.index("Rose"))

#7. ✅ Reverse the original list
# reversed_names = pet_names.copy()
# reversed_names.reverse()
# print(reversed_names)


#8. ✅ Return the frequency of a given element 
# counter = pet_names.count("Rose")
# print(counter)

# Updating Lists
#9. ✅ Change the first element to all uppercase 
# pet_names_uppper = pet_names[0].upper()
# print(pet_names_uppper)


#10. ✅ Append a new name to the list
# pet_names.append("Mikey")
# print(pet_names)

#11. ✅ Add a new name at a specific index
# pet_names.insert(4, "Gijoe")
# print(pet_names)

#12. ✅ Add two lists together 
# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# list1.extend(list2)
# print(list1)

#13. ✅ Remove the final element from the list
# pet_names.pop()
# print(pet_names)

#14. ✅ Remove element by specific index
# pet_names.pop(1)
# print(pet_names)


#15. ✅ Remove a specific element 
# pet_names.remove("Luke")
# print(pet_names)

#16. ✅ Remove all pet names from the list
# pet_names.clear()
# print(pet_names)

#Tuple 
# 📚 Review With Students:
    # Mutable, Immutable, Changeable, Unchangeable

#17. ✅ Create a Tuple of pet 10 ages 
my_tuple = (12, 3, 6, 8, 7, 6, 5, 9, 4, 5)
# print(my_tuple)

#18. ✅ Print the first pet age
# print(my_tuple[0])

# Testing Changeability 
#19. ✅ Attempt to remove an element with ".pop" (should error)
# my_tuple.pop()

#20. ✅ Attempt to change the first element (should error)
# my_tuple[1] = 23
# print(my_tuple[1])

# Tuple Methods
#21. ✅ Return the frequency of a given element
# counter = my_tuple.count(6)
# print(counter)

#22. ✅ Return the index of a given element 
# print(my_tuple.index(7))

#23. ✅ Create a Range 
#Note:  Ranges are primarily used in loops
# range = range(10)
# print(range)

# Demo Sets (Stretch Goal)
#24. ✅ Create a set of 3 pet foods


# Demo Dictionaries 
# Creating 
#25. ✅  Create a dictionary of pet information with the keys "name", "age" and "breed"
pet_info_rose = {'name':'rose','age':11,'breed':'domestic long '}


#26. ✅  Use dict to create a dictionary of pet information with the keys "name", "age" and "breed"
pet_info_spot = dict(name='Spot', age=25, breed='boxer')



# Reading
#27. ✅ Print the pet attribute of "name" using bracket notation 
# print(pet_info_rose["name"])

#28. ✅ Print the pet attribute of "age" using ".get"
#Note: ".get" is preferred over bracket notation in most cases because it will return "None" instead of an error
# print(pet_info_spot.get('age'))

# Updating 
#29. ✅ Update the pets age to 12
# pet_info_spot['age'] = 12
# print(pet_info_spot)

#30. ✅ Update the other pets age to 26
# pet_info_rose['age'] = 26
# print(pet_info_rose)

# Deleting
#30. ✅ Delete a pets age using the "del" keyword 
# del pet_info_spot['age']
# print(pet_info_spot)

#31. ✅ Delete the other pets age using ".pop"
# pet_info_rose.pop('age')
# print(pet_info_rose)

#32. ✅ Delete the last item in the pet dictionary using "popitem()"
# pet_info_spot.popitem()
# print(pet_info_spot)


# Demo Loops 
pet_info = [
    {
        'name':'rose',
        'age':11,
        'breed': 'domestic long-haired',
    }, 
    {
        'name':'spot',
        'age':25,
        'breed': 'boxer',
    },
    {
        'name':'Meow Meow Beans',
        'age':2,
        'breed': 'domestic long-haired',
    }
    ]

#33. ✅ Loop through a range of 10 and print every number within the range
# for i in range(10):
#     print(i)

#34. ✅ Loop through a range between 50 and 60 that iterates by 2 and print every number
# for i in range(50, 60, 2):
#     print(i)

#35. ✅ Loop through the "pet_info" list and print every dictionary 
# for dict in pet_info:
#     print(dict)


#36. ✅ Create a function that takes a list as an argument 
    # The function should use a "for" loop to loop through the list and print every item 
    # Invoke the function and pass it "pet_names" as an argument
# def print_item(list):
#     for item in list:
#         print(item)
# print_item(pet_names)


#37. ✅ Create a function that takes a list as an argument. (simple example) 
    # The function should define a counter and set it to 0
    # Create a "while" loop 
        # The loop will continue as long as the counter is less than the length of the list
        # Every loop should increase the count by 1
    # Return the counter 

# def counter_function(list):
#     counter = 0
#     while counter < len(list):
#         counter += 1
#     print(counter)
# counter_function(pet_info)


#38. ✅ Create a function that updates the age of a given pet
        # The function should take a list of "dict"s, "name" and "age" as parameters 
        # Create am index variable and set it to 0
        # Create a while loop 
            # The loop will continue so long as the list does not contain a name matching the "name" param and the index is less then the length of the list
            # Every list will increase the index by 1
        # If the dict containing a matching name is found, update the item's age with the new age 
            # Otherwise, return 'pet not found'

# def update_pet_age(list, name, age):
#     index = 0
#     while index < len(list) and list[index]["name"] != name:
#         index += 1
#     if index < len(list):
#         list[index]['age'] = age
#         return list[index]
#     else:
#         return 'pet not found'
    
# print(update_pet_age(pet_info, "spot", 27))


# map like 
#39. ✅ Use list comprehension to return a list containing every pet name from "pet_info" changed to uppercase
# uppercase_list = [pet["name"].upper() for pet in pet_info]
# print(uppercase_list)

# find like
#40. ✅ Use list comprehension to find a pet named spot
# find_spot = [pet for pet in pet_info if pet["name"] == "spot"]
# print(find_spot)

# filter like
#41. ✅ Use list comprehension to find all of the pets under 3 years old
# find_pets = [pet for pet in pet_info if pet["age"] < 3]
# print(find_pets)

#43. ✅ Create a generator expression matching the filter above. Compare and contrast the generator to the list comprehension. 
# find_pets_generator = (pet for pet in pet_info if pet["age"] < 3)
# for pet in find_pets_generator:
#     print(pet)
