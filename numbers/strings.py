
# can declare string in single or double quotes
name = "Tharangini"
color = 'black'
print(name)
print(color)

print("\n")
# triple quotes """ """ -> to print msg like email
message = f""" 
          Hello {name}
          welcome to Python learning
          Glad to have you here"""
print(message)

# indexing
# getting a letter from string
program = "python"
print(program[0])
print(program[1])

# -1 last index and counts from last
print(program[-1])
print(program[-2])


# slicing
# letters
# doesnt count last index of selected range
print(program[0: 3])
print(program[0: ])
# even if you dont mention, counts from 0th index
print(program[ : 5])

# length of index
print(program[ : ])

# multiplication
letters = "abc"
my_string = letters * 3
print(my_string)

# escape chara
program = "Hello\nWorld"
print(program)