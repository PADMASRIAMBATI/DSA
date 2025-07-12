import random

print(help(random))
low = 1
high = 100
number = random.randint(low, high)
print(number)

num = random.random()
print(num)

options = ("rock", "paper", 'scissor')
option  = random.choice(options)
print(option)

cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
random.shuffle(cards)
print(cards)