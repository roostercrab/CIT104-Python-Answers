first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
age = int(input("Enter your age: "))
confidence = int(input("What confidence do you have in programmers? (1-100): "))
dog_age = age * 7
print("Hello " + first_name + " " + last_name + ", nice to meet you! You might be "
      + str(age) + " in human years, but in dog years you are " + str(dog_age) + ".")

# -------- Extra credit  -------- 
if (confidence/100) < .5:
    print("I agree, programmers can't be trusted!")
else:
    print("Writing good code takes hard work!")
