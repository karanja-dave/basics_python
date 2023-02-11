#compose message using f-strings
name = "dave"
print(f"Hello {name.title()}, would ypu like to leran some python today?")
print(name.title())
print(name.upper())
print(name.lower())
#compose message and assign variable
f_n = "dave"
l_n = "karanja"
f_p = f"{f_n} {l_n}"
message = f'{f_p.title()} once said,"A person who never made a mistake never tried anything new"'
print(message)
#
name = '\tdave\n\tkaranja\t'
print(name)
print(name.strip())