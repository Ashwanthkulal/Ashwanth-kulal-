print( "love")

girl_name = input("girl_name: ")
girl_age = int(input("girl_age: "))
boy_name = input("boy_name: ")
boy_age = int(input("boy_age: "))

age_diff = abs(girl_age - boy_age)

print( boy_name + " loves " + girl_name + ". age difference is " + str(age_diff ))

  #formatted strings
print(f"{boy_name} loves {girl_name}. age difference is {age_diff}")