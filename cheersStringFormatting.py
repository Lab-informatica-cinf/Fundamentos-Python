#!/usr/bin/python3

''' 
This script receive a person name, 
and return "hello "person name", 
welcome to labcinf2020"
This code could ask me name twice. one for instructions
other for the main function, if this are activate.
'''

#basic variable declaration,data input, data store, and  print instruction.
person_name = input('what its your name?')

cheers = 'hello %s, welcome to Labcinf2020' % person_name

print(cheers)

#create a function that encapsulate above instructions.

def cheers_string_formatting():

	'''function that encapsulate code. whit out 
	   input params. output is print here. 
	'''

	person_name = input('what its your name?')

	cheers = 'hello %s, welcome to Labcinf2020' % person_name

	print(cheers)


def main():
	cheers_string_formatting()

if __name__ == '__main__':
	#main()			#uncomment main for activate main function, ask twice.
	print("enjoy it! :)")
