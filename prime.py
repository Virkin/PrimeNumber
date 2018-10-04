# A program that looks for prime numbers

from time import clock
from math import sqrt

from colorama import Fore
from colorama import Style

def isPrime(number) :
	"""	Checks if the number is prime
		Return True if it is a prime number, else return False""" 
	
	# First we checks some standard conditions
	if number == 2 or number == 3 : # 2 is prime
		return True
	elif number == 1 or number%2 == 0 or number%3 == 0 : 
		return False

	"""	Below, we use the fact that prime number are in the form 6K ± 1
		So we start with 5 as a divisor, then we add 2 or 4 altertively to test if the number can be divide by potential prime number
		As we have already treated the cases of even numbers and the case of numbers which can be divided by 3, 
		this number can only be divided by prime numbers if it is not a prime number itself."""
	
	divisor = 5
	incValue = 2
	
	while divisor <= sqrt(number) : # If the divisor is greater than the square root of the number, then it cant divide the number
		if number%divisor == 0 : # If the number can be divide by the divisor, then the number is not a prime
			return False
		
		divisor += incValue
		incValue = 6 - incValue
	
	return True

if __name__ == '__main__': 
	# The main is doing a speed test of the "isPrime" function
	
	print(f"{Fore.BLUE}\n =============================== Prime speed test ==============================")
	print(f" This is a speed test for a function that determines if a number is prime or not {Style.RESET_ALL}")
	
	while True :
		try :
			minNumber = int(input(f"{Fore.YELLOW}\n Min number : {Style.RESET_ALL}")) # The min number which the program will tests
			maxNumber = int(input(f"{Fore.YELLOW}\n Max number : {Style.RESET_ALL}")) # The max number which the program will tests

			if maxNumber < minNumber :
				raise Exception(f"{Fore.RED} The max number have to be greater than the minimum !{Style.RESET_ALL}")
			break;
		except ValueError as e:
			print(f"{Fore.RED} Please type a correct number !{Style.RESET_ALL}")
			continue
		except Exception as e:
			print(e)
			continue
			

	timer = clock() # Start of the timer

	number = minNumber
	incPrime = 0 # The total number of prime

	while number <= maxNumber : 
		if isPrime(number) == True : 
			incPrime += 1 # Increments the total number of prime if the number is a prime
		number += 1 # Increments the actual number

	
	timer = round(clock() - timer, 2) # End of the timer

	print(f"\n{Fore.BLUE} Time : {Style.RESET_ALL}{timer}") # Print the time that has been taken to perform the task
	print(f"{Fore.BLUE} Number of prime number between {minNumber} and {maxNumber} : {Style.RESET_ALL}{incPrime}") # Print the total of prime number which have been found sub the max

	print(f"""\n{Fore.GREEN} 'Mathematicians have tried in vain to this day to discover some order in the sequence of prime numbers, 
 and we have reason to believe that it is a mystery into which the human mind will never penetrate.', Leonhard Euler\n{Style.RESET_ALL}""") # A quote about prime number :)


