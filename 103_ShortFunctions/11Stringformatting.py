name = "durgesh"
greeting = f"hello {name}"
name = "vishal"  # It will not change dynamically so u have to write greeting again
print(greeting)

print(f"Hello {name}")

# --------------or use . format()---------------------

greetme = "hello {} how are {}" # Create a Template
formatted = greetme.format("Dugresh","you") # use .format function on it.
print(formatted)

