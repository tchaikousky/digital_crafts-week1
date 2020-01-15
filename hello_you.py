#prompts user for their name, then says 'hello' and tells them the length of their name.

name = input("What is your name? ")
print("Hello, %s" % name)
print("Your name has " + len(name) + " letter in it! Awesome")