# <---The init Method--->
class User: 
	def __init__(self, first, last, age):
		self.first = first
		self.last = last
		self.age = age

user1 = User('Tanner', 'Langlinais', 26)
user2 = User('Trevor', 'Langlinais', 23)
print(user1.first, user1.last)
print(user2.first, user2.last)

# <---Underscores--->
class Person:
	def __init__(self):
		self.name = 'Tony'
		self._secret = 'hi'
		self.__msg = 'I like turtles!'

	# def doorman(self, guess):
	# 	if guess == self._secret:
	# 		#let them in

p = Person()

print(p.name)
print(p._secret)
# print(p.dir(p))
print(p._Person__msg)

# Adding Instance Methods
class User: 
	def __init__(self, first, last, age):
		self.first = first
		self.last = last
		self.age = age

	def full_name(self):
		return f'{self.first} {self.last}'

	def initials(self):
		return f'{self.first[0]}.{self.last[0]}.'

	def likes(self, thing):
		return f'{self.first} likes {thing}'

	def is_senior(self):
		return self.age >= 65

user1 = User('Tanner', 'Langlinais', 26)
user2 = User('Trevor', 'Langlinais', 23)
print(user1.first, user1.last)
print(user2.first, user2.last)
print(user1.is_senior())

# Ex. 78
class BankAccount:
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0.0
        
    def deposit(self, amount):
        self.balance += amount
        return self.balance
        
    def withdraw(self, amount):
        self.balance -= amount
        return self.balance

# Chicken Coop Exercise
class Chicken:
    total_eggs = 0
    
    def __init__(self, species, name):
        self.eggs = 0
        self.species = species
        self.name = name
    
    def lay_egg(self):
        self.eggs+=1
        Chicken.total_eggs+=1
        return self.eggs