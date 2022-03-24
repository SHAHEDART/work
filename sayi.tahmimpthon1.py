import random
import math
# Taking Inputs
lower = int(input("sayının alt sınırı gir:- "))

# Taking Inputs
upper = int(input("sayının üst sınırı gir:- "))

# generating random number between
# the lower and upper
x = random.randint(lower, upper)
print("\n\t sen sadece ",
	round(math.log(upper - lower + 1, 2)),
	" tahmin etmek için şans!\n")

# Initializing the number of guesses.
count = 0

# for calculation of minimum number of
# guesses depends upon range
while count < math.log(upper - lower + 1, 2):
	count += 1

	# taking guessing number as input
	guess = int(input("bir sayi tahmin et:- "))

	# Condition testing
	if x == guess:
		print("tebrikler bu kadar denemeyle yaptin ",
			count, " ...")
		# Once guessed, loop will break
		break
	elif x > guess:
		print("çok düşük tutun!")
	elif x < guess:
		print("çok yüksek tutun!")

# If Guessing is more than required guesses,
# shows this output.
if count >= math.log(upper - lower + 1, 2):
	print("\ntahmin edilen sayi %d" % x)
	print("\tsonraki sefere iyi şanslar!")

# Better to use This source Code on pycharm!
           
            
