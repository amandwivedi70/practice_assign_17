# 1. Write a python program to store all the programming languages known to you using Set.

s = {"Java", "Python", "Dart", "Javascript", "C", "C++", "Flutter"}

print(s)

# 2. Write a python program to store your own information {name, age, gender, so on..}


name = 'Aniket'
age = 21
gender = 'male'
college = 'Government college of engineering karad'

s1 = {name, age, gender, college}

print(s1)

# 3. Write a python script to get the data type of a Set.
s = {"Java", "Python", "Dart", "Javascript", "C", "C++", "Flutter"}
print(type(s))

# 3. Write a python script to get the data type of a Set.
s = {"Java", "Python", "Dart", "Javascript", "C", "C++", "Flutter"}
print(type(s))

# 4. Write a Python script to find if “Python” is present in the set  thisset = {"Java", "Python", "Django"}

thisset = {"Java", "Python", "Django"}

if "Python" in thisset:
    print("Present")
else:
    print("Not Present")

# 4. Write a Python script to find if “Python” is present in the set  thisset = {"Java", "Python", "Django"}

thisset = {"Java", "Python", "Django"}

if "Python" in thisset:
    print("Present")
else:
    print("Not Present")

# 5. Write a python program to add items from another set to the current set. thisset = {"Java", "Python", "SQL"} secondset = {"C", "Cpp", "NoSQL"}

s1 = {"Java", "Python", "SQL"}
s2 = {"C", "Cpp", "NoSQL"}

s1.update(s2)

print(s1)


# 6. Write a python program to add elements of list to a set thisset = {"Python", "Django", "JavaScript"} mylist = ["Java", "C"]

S = {"Python", "Django", "JavaScript"}
l = ["Java", "C"]

S.update(l)
print(S)

# 7. Write a python program to remove last item of the given set thisset = {"Python", "Django", "JavaScript", “SQL”}

thisset = {"Python", "Django", "JavaScript", "SQL"}

thisset.remove("SQL")

print(thisset)


# 8. Write a python program to delete the set completely.
thisset = {"Python", "Django", "JavaScript", "“SQL”"}

thisset.clear()

print(thisset)

# 9. Write a python program to loop through the set and print values thisset = {"Python", "Django", "JavaScript", “SQL”}

thisset = {"Python", "Django", "JavaScript", "SQL"}
print()
for i in thisset:
    print(i, end='->')

# 10. Write a python program to find the maximum and minimum value in a set.

s1 = {10, 20, 33, 199, 102, 10, 155, -50}
print()
print(s1)

print('Max : ', max(s1))
print('Min : ', min(s1), end='')