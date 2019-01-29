# --------------------------------- Exercise --------------------------------- #

pennies = int(input("How many pennies do you have? "))
nickels = int(input("How many nickels do you have? "))
dimes = int(input("How many dimes do you have? "))
quarters = int(input("How many quarters do you have? "))
halfDollars = int(input("How many half dollars? do you have? "))
oneDollars = int(input("How many one dollars do you have? "))
print("You have " + str(pennies) + " pennies.")
print("You have " + str(nickels) + " nickels.")
print("You have " + str(dimes) + " dimes.")
print("You have " + str(quarters) + " quarters.")
print("You have " + str(halfDollars) + " half dollars.")
print("You have " + str(oneDollars) + " one dollars.")
total = pennies + (5 * nickels) + (10 * dimes) + (25 * quarters) + (50 * halfDollars) + (100 * oneDollars)    
print("The value of all your coins is $" + str(total/100) + ".")

# --------------------------------- Exercise with extra credit --------------------------------- #

pennies = int(input("How many pennies do you have? "))
nickels = int(input("How many nickels do you have? "))
dimes = int(input("How many dimes do you have? "))
quarters = int(input("How many quarters do you have? "))
halfDollars = int(input("How many half dollars? do you have? "))
oneDollars = int(input("How many one dollars do you have? "))
if pennies == 1:
        p = " penny"
else:
        p = " pennies"
print("You have " + str(pennies) + p + ".")
if nickels == 1:
        n = " nickel"
else:
        n = " nickels"
print("You have " + str(nickels) + n + ".")
if dimes == 1:
        d = " dime"
else:
        d = " dimes"
print("You have " + str(dimes) + d + ".")
if quarters == 1:
        q = " quarter"
else:
        q = " quarters"
print("You have " + str(quarters) + q + ".")
if halfDollars == 1:
        h = " half dollar"
else:
        h = " half dollars"
print("You have " + str(halfDollars) + h + ".")
if oneDollars == 1:
        o = " one dollar"
else:
        o = " one dollars"
print("You have " + str(oneDollars) + o + ".")
total = pennies + (5 * nickels) + (10 * dimes) + (25 * quarters) + (50 * halfDollars) + (100 * oneDollars)    
print("The value of all your coins is $" + str(total/100) + ".")

