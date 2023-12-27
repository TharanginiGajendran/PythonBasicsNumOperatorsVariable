
# bitwise works only with bits(binary digits)
# decimal numbers
a = 10
b = 5

# AND & -> returns 1 if both are 1, else returns 0
print(a & b)
c = bin(a & b)
print(c)

# OR | -> returns 1 if any of the value is 1, else returns 0

x = 6
y = 9
# 1111 is 15 in decimal, so returns 15
print(x | y)
print(bin(x | y))

x = 1
y = 2
print(x / y)
print(x % y)

x = 15
print(bin(25))


# Not ~ -> basically means reversing
print("************** Not ~")
print(bin(10))

# add sign bi 0 (01010) -> returns positive number
# sign bit is 1 -> negative number
# positional weigh of sign bit 1 is negative value
num = 5
print(bin(num))
print(bin(6))
print(bin(11))
print(~num)


num = 4
print(bin(num))
print(~num)

# XOR ^ -> if anyone is 1 get 1, if both are 1 will get 0, else 0
print("*************************")
n1 =10
n2 = 9
print(bin(10))
print(bin(9))
print(f"xor {n1 ^ n2}")
print(f"or {n1 | n2}")
print(bin(3))
print("**************************")


a1 = 5
b1 = 8
print(bin(5))
print(bin(8))
print(a1 ^ b1)
print(a1 | b1)
print(bin(11))