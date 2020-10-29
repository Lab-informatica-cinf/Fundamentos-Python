#!/usr/bin/python3

'''
This script implement other python string formating.
util for handle string varaibles dinamically.

input: name, question
oput: "hello, {name}, how's it {question}?"
'''


name = input('insert name:')                   # input data, store in str type

question = input('inser question')

greet = f"hello, {name}, how's it {question}?" # store variable, type str.

print(greet) 								   # instruction; print() is built-in function.                                  

def greetStringFormating():

	'''this function encapsulate above things;
		whitout input params. 
		output : print greet varaible content.
	'''

	name = input('insert name:')

	question = input('inser question')

	greet = f"hello, {name}, how's it {question}?"

	print(greet)

def main():
	greetStringFormating()

if __name__ == '__main__':
	main()