zoo = ("red panda", "kitten", "turtle", "slug", "monkey", "zebra", "chipmunk" "dog", "moose", "alpaca", "dolphin")

print(zoo.index("kitten"))

# Determine if an animal is in your tuple by using value in tuple syntax.
animal_to_find = "kitten"

if animal_to_find in zoo: 
    print(f"{animal_to_find} was found!")


(first_animal, second_animal, third_animal, fourth_animal, fifth_animal, sixth_animal, seventh_animal, eighth_animal, ninth_animal, tenth_animal) = zoo
print(first_animal)

animal_list = list(zoo)

animal_list.extend(["wolf", "fox", "narwhal"])
# have to store list in a new variable in order to change to a tuple
new_animals = tuple(animal_list)

print(new_animals) 