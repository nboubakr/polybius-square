#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Filename: main.py

# Polybius Square [Square 5x5, Removed Letter: 'W']
# University of Djillali Liabes (UDL) - Sidi Bel Abbes
# Faculty of Sciences - Computer Science (LMD1) 2011/2012 
# Student: Boubakr NOUR <n.boubakr@gmail.com>

# License: Academic Free License (AFL)

import os

from polybius import Polybius

def clear():
	"""Function to clear the Terminal (Console), works under Windows, Mac OS, *Unix"""
	os.system(['clear', 'cls'][os.name == 'nt'])

def main_menu():
	"""Procedure to display the main menu"""
	clear()
	print ("""
	| * * * WELCOME TO THE POLYBIUS SQUARE ENCIPHER/DECIPHER * * * |
	 __________________________ MAIN MENU _________________________
	|                                                              |
	|                                                              |
	|    (*) To view the instructions, Press <I>                   |
	|    (*) To encipher a plaintext, Press <E>                    |
	|    (*) To decipher a ciphertext, Press <D>                   |
	|    (*) To quit the script, Press <Q>                         |
	|                                                              |
	|______________________________________________________________| 
	""")

def instructions():
	"""Procedure to display the script instructions."""
	clear()
	print ("""
	 ________________________ INSTRUCTIONS ________________________
	|                                                              |
	|                                                              |
	|   (*) The diagram of the Polybius Square 5x5:                |
	|       A B C D E                                              |
	|       F G H I J                                              |
	|       K L M N O                                              |
	|       P Q R S T                                              |
	|       U V X Y Z                                              |
	|   (*) Each letter can be represented by a group of two       |
	|       numbers: that of his line and that of his column.      |
	|       So "A"=11, "E"=15, "U"=51 ...                          |
	|                                                              |
	|______________________________________________________________|
	""")

def quit():
	"""Procedure to display quit message"""
	clear()
	print ("""
	 _________ QUIT THE POLYBIUS SQUARE ENCIPHER/DECIPHER _________
	|                                                              |
	|                                                              |
	|  THANK YOU FOR USING THIS CRYPTOGRAPHY !                     |
	|  ---------------------------------------                     |
	|                                                              |
	|  (*) University of Djillali Liabes (UDL) - Sidi Bel Abbes    |
	|                                                              |
	|  (*) Faculty of Sciences - Computer Science (LMD1) 2011/2012 |
	|                                                              |
	|  (*) Student: Boubakr NOUR <n.boubakr@gmail.com>             |
	|                                                              |
	|______________________________________________________________|
	""")

def error(msg=''):
	"""Procedure to display an error message"""
	clear()
	print ("""
	 ______                        _ 
	|  ____|                      | |
	| |__   _ __ _ __ ___  _ __   | |
	|  __| | '__| '__/ _ \| '__|  | |
	| |____| |  | | | (_) | |     |_|
	|______|_|  |_|  \___/|_|     (_)
	

	""", msg)

def main():
	main_menu()	# Main Menu
	myPolybius = Polybius()

	try:
		main_choice = input('[+] Enter your choice: ').lower().strip()
	except:
		main()
	
	if main_choice == 'i':		# Instructions
		instructions()
		
		input('Press <Enter> to return to the main menu... ')
		main()
		
	elif main_choice == 'e':	# Encipher
		clear()
		print("\v\tEnter your plaintext to encipher: ")
		try:
			sentence = input("--> ")
		except KeyboardInterrupt:
			main()

		print("\v\tYour ciphertext is: \n")
		myPolybius.encipher(sentence)
		
		input('\n\vPress <Enter> to return to the main menu... ')
		main()
	
	elif main_choice == 'd':	# Decipher
		clear()
		print("\v\tEnter your ciphertext to decipher: ")

		try:
			sentence = input("--> ")
		except KeyboardInterrupt:
			main()
		
		print("\v\tYour message decrypted is: ")
		myPolybius.decipher(sentence)

		input('\n\nPress <Enter> to return to the main menu... ')
		main()
	
	elif main_choice == 'q':	# Quit
		quit();
		input("	----------------------------------------------------------------")
		exit(0)
	
	else:
		error("I didn't understand your choice !\n")
		input('Press <Enter> to try again... ')
		main()

if __name__ == '__main__':
	main()

# EOF
