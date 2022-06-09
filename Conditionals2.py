# EXAMPLE 1
#my_boolean = False

#if my_boolean:
 #   print("Not gonna print")
  #  else:
   #     print("Boolean is false")

    # will return "Boolean is false at first if statement won't trigger"

#my_boolean = True
#my_boolean2 = False

#if my_boolean:
  #  if my_boolean2:
   #     print("Both True")
    #    else:
     #       print("1st true and 2nd false")
      #      else:
       #         print("Boolean is false")

# EXAMPLE 2

my_boolean = False

if my_boolean:
    print("My boolean is truthy!")
else:
    print("My boolean is not truthy...")

my_money = 10

if my_money < 10:
    print("sort yourself out")
else:
    print("Nice")

# EXAMPLE 3

deposit = 100
password = "password"

if 0 < deposit <= 100 and password == "password":
  print(f"thank you for depositing {deposit}") # thank you for depositing 100
else:
  print("failure")

# EXAMPLE 4

name = "Elina"
name1case = name.lower()

if name1case in ("Elina", "admin"):
    print("Unacceptable Username")
else: 
   print(f"Welcome {name}")

age = int(input("Give us your age: "))
if age >= 85:
    print("85 or older")
elif age >= 65:
        print("Between 65 and 85")
elif age >= 45:
        print("Between 45 and 65")
else:
            print("Young")