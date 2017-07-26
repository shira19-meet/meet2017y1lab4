weekday = input("is it a weekday today?")

if weekday == "yes":
    strawberries=int(input("how many strawberries do you have?"))
    if strawberries>39 and strawberries<61:
        print("fun")
    else:
        print("not fun")
if weekday=="no":
    strawberries=int(input("how many strawberries do you have?"))
    if strawberries>39:
        print("fun")
    else:
        print("not fun")
