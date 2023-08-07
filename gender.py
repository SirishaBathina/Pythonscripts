def get_honorific(age, gender):
    if gender == 'male':
        if age < 18:
            return "Young Master"
        else:
            return "Mr."
    elif gender == 'female':
        if age < 18:
            return "Young Miss"
        else:
            return "Ms."
    else:
        return "Mx."  # Gender-neutral honorific
age = int(input("Enter person's age: "))
gender = input("Enter person's gender (male/female): ")

honorific = get_honorific(age, gender)
print("Honorific:", honorific)
