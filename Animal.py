                                                                                                                                                animal = "cat"
animal_sounds = {
    "cat": "Meow",
    "dog": "Woof",
    "cow": "Moo",
    "duck": "Quack"
}
if animal in animal_sounds:
    sound = animal_sounds[animal]
    print(f"The {animal} makes the sound: {sound}")
else:
    print(f"Sorry, I don't know the sound of the {animal}.")
