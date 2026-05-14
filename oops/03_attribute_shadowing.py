class Chai:
    temperature = "hot"
    strength = "Strong"

cutting = Chai()
print(cutting.temperature)

cutting.temperature = "Mild"
cutting.cup = "small"
print("After changing ", cutting.temperature)
print("Cup Size ", cutting.cup)
print("Direct look into the class ", Chai.temperature)

del cutting.temperature
del cutting.cup 
print(cutting.temperature) # will fallback to default value
print (cutting.cup) # error cause there is not fallback value