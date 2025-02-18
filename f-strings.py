# string formatting
# using the format method
txt1 = 'For only {price} rupees'
print(txt1.format(price = 49))   # feeding price after the string

txt2 = 'For only {price} rupees'
print(txt2.format(price = 49.99))

txt3 = 'For only {price:.2f} rupees'
print(txt3.format(price = 49.999))

letter = "Hey my name is {1} and I am from {0}"
country = "India"
name = "Harry"
print(letter.format(country, name))
print(f"Hey my name is {name} and I am from {country}")

# f-string
# new string formatting mechanism introduced by the PEP 498
# also known as Literal String Interpolation
val = 'Geeks'  
print(f"{val}for{val} is a portal for {val.lower()}.")  
name = 'Shefali'  
age = 23  
print(f"Hello, My name is {name} and I'm {age} years old.")

# f-string evaluates at runtime; we can put all valid Python expressions in them

# special case
op = 2*30
print(op)
print(type(op))
print('op')
print(type('op'))
print(f"{2 * 30}")
print(type(f'{op}'))