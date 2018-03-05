# ask for input
# input comes as STRING - needs to be INT
# age = input("How old are you? ")
# if age != "":
# 	age = int(age)

# # 18-21 needs a wristband
# if age >= 18 and age < 21:
# 	print("You can enter, but need a wristband!")

# # 21+
# elif age >= 21:
# 	print("You are good to enter and can drink!")

# # too young
# else:
# 	print("You can't come in, little one! :(")

# more efficent way
age = input("How old are you? ")
if age != "":
	age = int(age)

if age >= 21:
	print("You are good to enter and can drink!")

elif age >= 18:
	print("You can enter, but need a wristband!")

else:
	print("You can't come in, little one! :(")