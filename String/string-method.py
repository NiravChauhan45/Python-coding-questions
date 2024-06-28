a = "!!!Nirav Chauhan Nirav Chauhan nirav!!!!!!!!!!!"
print(len(a))
print(a.upper())
print(a.lower())
print(a.rstrip("!"))
print(a.lstrip("!"))
print(a.strip("!"))
print(a.replace("Nirav","Yash"))
print(a.strip("!").split(" "))

blogHeading = "introduction to js"
print(blogHeading.capitalize())

str1 = "Welcome to the Console!"
print(len(str1))
print(len(str1.center(50)))

print(a.count("nirav"))

print(a.endswith("!!"))

str1 = "Welcome to the Console !!!"
print(str1.endswith("to",4,10))

str1 = "He's name is Nirav. He is an honest man"
print(str1)
print(str1.find("is"))
print(str1.index("is"))

str1 = "WelcomeToTheConsole"
print(str1.isalnum()) # Alpha-Numeric = A-Z,a-z,0-9
print(str1.isalpha()) # Alphabats = A-Z,a-z

print(str1.islower()) # return true if string is lower otherwise return flase
print(str1.isupper()) # return true if string is upper otherwise return flase

str1 = "We wish you a Merry Christmas\n" 
print(str1.isprintable())

str1=" "
print(str1.isspace())

str1 = "World Health Organization"
print(str1.istitle())

str1 = "Python is a Interpreted Language"
print(str1.startswith("Python"))

str1 = "Python is a Interpreted Language"
print(str1.swapcase()) # convert lower to upper and upper to lower