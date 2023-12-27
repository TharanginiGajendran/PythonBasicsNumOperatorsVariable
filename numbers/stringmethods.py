
# why its called string methods -> only be used with the presence of string
# these are also called methods
name = "Tharangini"
print(name.upper())
print(name.lower())



print("\n")
print("********************properties of string")
# generic functions -> dont need to be used with strings or numbers can be used separtely
# len() -> length of string
# len(),type(),int(),print()
print(len(name))

print("\n")
# find()-> returns the index of string
print("*******************8")
my_name = "Thara"
print(my_name.find("a"))
print("********************")

print("\n")
# replace() -> to replace a character or sequence of char
# case sensitive
name = "Thara"
print(name.replace("Thara","Tharangini"))

country = "korea"
print(country.replace("korea","south korea"))

# in -> to find the existence of charcter
# case sensitive
course = "Python for Beginners"
print("Python" in  course)