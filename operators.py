# Arithmetic Operators
a = 10
b = 5
print("Arithmetic Operators")
print(f"{a} + {b} = {a + b}")  # Addition
print(f"{a} - {b} = {a - b}")  # Subtraction
print(f"{a} * {b} = {a * b}")  # Multiplication
print(f"{a} / {b} = {a / b}")  # Division
print(f"{a} % {b} = {a % b}")  # Modulus
print(f"{a} ** {b} = {a ** b}")  # Exponentiation
print(f"{a} // {b} = {a // b}")  # Floor Division
print()

# Comparison Operators
print("Comparison Operators")
print(f"{a} == {b} is {a == b}")  # Equal
print(f"{a} != {b} is {a != b}")  # Not Equal
print(f"{a} > {b} is {a > b}")  # Greater Than
print(f"{a} < {b} is {a < b}")  # Less Than
print(f"{a} >= {b} is {a >= b}")  # Greater Than or Equal To
print(f"{a} <= {b} is {a <= b}")  # Less Than or Equal To
print()

# Logical Operators
x = True
y = False
print("Logical Operators")
print(f"{x} and {y} is {x and y}")  # Logical AND
print(f"{x} or {y} is {x or y}")  # Logical OR
print(f"not {x} is {not x}")  # Logical NOT
print()

# Bitwise Operators
print("Bitwise Operators")
print(f"{a} & {b} = {a & b}")  # Bitwise AND
print(f"{a} | {b} = {a | b}")  # Bitwise OR
print(f"{a} ^ {b} = {a ^ b}")  # Bitwise XOR
print(f"~{a} = {~a}")  # Bitwise NOT
print(f"{a} << 1 = {a << 1}")  # Bitwise Left Shift
print(f"{a} >> 1 = {a >> 1}")  # Bitwise Right Shift
print()

# Assignment Operators
c = 10
print("Assignment Operators")
c += 5  # Equivalent to c = c + 5
print(f"c += 5: c = {c}")
c -= 3  # Equivalent to c = c - 3
print(f"c -= 3: c = {c}")
c *= 2  # Equivalent to c = c * 2
print(f"c *= 2: c = {c}")
c /= 4  # Equivalent to c = c / 4
print(f"c /= 4: c = {c}")
c %= 3  # Equivalent to c = c % 3
print(f"c %= 3: c = {c}")
c **= 2  # Equivalent to c = c ** 2
print(f"c **= 2: c = {c}")
c //= 2  # Equivalent to c = c // 2
print(f"c //= 2: c = {c}")
print()

# Membership Operators
list_var = [1, 2, 3, 4, 5]
print("Membership Operators")
print(f"3 in list_var is {3 in list_var}")  # in
print(f"6 in list_var is {6 in list_var}")  # in
print(f"6 not in list_var is {6 not in list_var}")  # not in
print()

# Identity Operators
print("Identity Operators")
d = a
print(f"a is d is {a is d}")  # is
print(f"a is not b is {a is not b}")  # is not
