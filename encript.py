# imports necessary functions.
import random
from math import factorial


# gives the ending information after the file has been encrypted or decrypted.
def finalConformation(choice, password, alphabet):
	if choice == "e":
		print ""
		print "your file has been created and it contains your encrypted message"
		print ""
		print nPr(len(alphabet), len(password))
		print ""
		print "please note that this is only right if your password does"
		print "not have any repeating letters, numbers, or characters"
		print ""
	else:
		print ""
		print "your file has been created and it contains your decrypted message"
		print ""


# get name of input and output file and the password.
def getInformation(choice):
	if choice == "e":
		print "What is the name of your source_file"
		sourceFile = getInput()
		print "What do you want the new file to be called"
		destinationFile = getInput()
		print "What do you want your password to be"
		password = getInput()
	elif choice == "d":
		print "What is the name of your source_file"
		sourceFile = getInput()
		print "What do you want the new file to be called"
		destinationFile = getInput()
		print "What was the password, if this is wrong the decryption will not work"
		password = getInput()

	return (sourceFile, destinationFile, password)


# collects user input.
def getInput():
    return raw_input("> ")

# part of nPr function.
def product(iterable):
    prod = 1
    for n in iterable:
        prod *= n
    return prod


# uses a permutation to get number of possible passwords.
def nPr(n , r):
    assert 0 <= r <= n
    x = product(range(n - r + 1, n + 1))
    return "your password length has about %s different combanations" % str(x)


# the code for the caesarian verson of the encrypt and decrypt program.
def caesarian(fin, fout, choice, alphabet):
    offset = random.randrange(1,len(alphabet))
    if choice=='d':
        offset = -offset
    print "Using the secret offset of", offset

    for line1 in fin:

        line2 = ""
        for c in line1:
            if c in alphabet:
                pos1 = alphabet.find(c)
                pos2 = (pos1+offset)%len(alphabet)
                line2 += alphabet[pos2]
                
        fout.write(line2)


# the code for the pseudo random verson of the encrypt and decrypt program.
def pseudoRandom(fin, fout, choice, alphabet, password):
    for line1 in fin:
        random.seed(password)
        offset = random.randrange(1,len(alphabet))
        if choice=='d':
            offset = -offset
        line2 = ""
        for c in line1:
            if c in alphabet:
                pos1 = alphabet.find(c)
                pos2 = (pos1+offset)%len(alphabet)
                line2 += alphabet[pos2]
        fout.write(line2)


# the code for the substitution verson of the encrypt and decrypt program.
def substitution(fin, fout, choice, alphabet, password):
    # encryption code.
	if choice == "e":
		alphabetList = []
		for x in alphabet:
			alphabetList.append(x)
		random.seed(password)
		random.shuffle(alphabetList)
		substitutionAlphabet = ""

		for i in alphabetList:
			substitutionAlphabet += i
		for i in fin:
			new_line = ""
			for j in range(len(i)):
				for k in range(len(alphabet)):
					if i[j] == alphabet[k]:
						new_line += alphabetList[k]
						break
			fout.write(new_line)
    # decryption code.
	elif choice == "d":

		alphabetList = []
		new_line = ""
		for x in alphabet:
			alphabetList.append(x)
		random.seed(password)
		random.shuffle(alphabetList)
		substitutionAlphabet = ""
		for i in alphabetList:
			substitutionAlphabet += i
		line = ""
		for line1 in fin:
			line += line1

		for i in line:
		
			for j in range(len(alphabetList)):
				if i == alphabetList[j]:
					new_line += alphabet[j]
					break
		fout.write(new_line)


# encription idea, under construction.
def multiplePasswords(fin, fout, choice, alphabet, passwordList):
	if choice == "e":
		alphabetList = []



		pass
	if choice == "d":
		pass


# lets you choose which version of the encryption/decryption you want to use.
def methodMenu():
	print """Which method do you want to use?
(c)aesarian fixed offset
(p)seudo-random offset
(s)ubstitution cipher"""
	choice = getInput()
	if choice == "c":
		return "c"
	elif choice == "p":
		return "p"
	elif choice == "s":
		return "s"
	else:
		methodMenu()


# lets you choose if you want to encrypt or decrypt.
def startMenu():
	print "Do you want to encrypt or decrypt?"
	print "(e)ncrypt"
	print "(d)ecrypt"
	print "(q)uit"
	choice = getInput()
	if choice == "q":
		return "q"
	elif choice == "e":
		return "e"
	elif choice == "d":
		return "d"
	else:
		startMenu()


# prints the description of the program.
def printDescription():
	print """This program encrypts and decrypts messages, using multiple encryption methods.
Input files must be in the same directory as this program.
Output files will be created in this same directory."""


def main():
	# defines the main alphabet.
	alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789,.?! \t\n\r"

	# calls the functions that will get the information that the program needs.
	printDescription()
	encryptOrDecrypt = startMenu()
	choice = methodMenu()

	# begins main loop.
	while 1:

		# if the chose to quit the program the loop breaks.
		if encryptOrDecrypt == "q":
			break

		# gets the input file and creates the output file to write to.
		sourceFile, destinationFile, password = getInformation(encryptOrDecrypt)

		fin = open(sourceFile, "rb")
		fout = open(destinationFile, "wb")

		# seeds the password into all random funtion methods.
		random.seed(password)

		# finds which encryption/decryption method was chosen.
		if choice == "c":
			caesarian(fin, fout, encryptOrDecrypt, alphabet)
		elif choice == "p":
				pseudoRandom(fin, fout, encryptOrDecrypt, alphabet, password)
		elif choice == "s":
			substitution(fin, fout, encryptOrDecrypt, alphabet, password)

		# closes input and output files.
		fin.close()
		fout.close()

		# tells user the the program has succsesfuly encrypted or decrypted the input files
		# also tell the user how many possible combinations there password length has.
		finalConformation(encryptOrDecrypt, password, alphabet)

		# ends the loop.
		break


# calling main to start the program.
if __name__ == "__main__":
	main()


