#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Filename: polybius.py

# Polybius Square [Square 5x5, Removed Letter: 'W']
# University of Djillali Liabes (UDL) - Sidi Bel Abbes
# Faculty of Sciences - Computer Science (LMD1) 2011/2012 
# Student: Boubakr NOUR <n.boubakr@gmail.com>

# License: Academic Free License (AFL)

import os

class Polybius:
	"""
	Polybius Square [Square 5x5, Removed Letter: 'W']
	"""
	def __init__(self):
		pass

	def __prepare_sentence__(self, sentence):
		"""Prepare a sentence for the encryption"""
		accent = ["âà", "éèêë", "îï", "ô", "ûü", "ç"]
		ascii = ["A", "E", "I", "O", "U", "C"]
		
		i = 0
		for word in accent: # Replacing accented characters possible
			for letter in word:
				sentence = sentence.replace(letter, ascii[i])
			i += 1
		for letter in "',-;:!?.":  # Remove punctuation
			sentence = sentence.replace(letter, "")
		sentence = sentence.upper()  # Passage in capitals letters
		return sentence

	def encipher(self, to_encrypt):
		"""Encipher a plaintext"""
		List_H, List_V = [], []
		for j in range(4):
			for i in range(5):
				List_H.append(chr(65+5*j+i))
			List_V.append(List_H)
			List_H = []
		List_H = []
		List_H.append(chr(85))
		List_H.append(chr(86))
		List_H.append(chr(88))
		List_H.append(chr(89))
		List_H.append(chr(90))
		List_V.append(List_H)
		
		to_encrypt = self.__prepare_sentence__(to_encrypt)
		to_encrypt = to_encrypt.replace(" ", "")  # Remove the space
		
		for i in range(len(to_encrypt)):
			pos = ord(to_encrypt[i])-65
			verti = str(int((pos/5)+1))
			hori = str((pos % 5)+1)
			fin = verti + hori
			print (fin, end=' ')
		print()

	def decipher(self, to_decrypt):
		"""Decipher a ciphertext"""
		List_H, List_V = [], []
		for j in range(4):
			for i in range(5):
				List_H.append(chr(65+5*j+i))
			List_V.append(List_H)
			List_H = []
		List_H = []
		List_H.append(chr(85))
		List_H.append(chr(86))
		List_H.append(chr(88))
		List_H.append(chr(89))
		List_H.append(chr(90))
		List_V.append(List_H)

		to_decrypt = to_decrypt.replace(" ", "")  # Remove the space
		length = len(to_decrypt)
		
		for h in range(0, length, 2):
			pos = int(to_decrypt[h])-1
			pos2 = int(to_decrypt[h+1])-1
			carac = List_V[pos][pos2]
			print(carac, end='')
		print()

# EOF