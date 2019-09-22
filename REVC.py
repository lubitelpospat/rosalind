import sys
import os
import re

from collections import Counter



DEBUG = False



def replacer(letter):
	if letter == "A":
		return "T"
	elif letter == "T":
		return "A"
	elif letter == "G":
		return "C"
	elif letter == "C":
		return "G"




def main():
	file_path = sys.argv[1]
	if (file_path[:2] != "./" and file_path[0] != "/" and file_path[:3] != "../" and file_path not in os.listdir()) and not  DEBUG:
		print("Fatal error: path not understood!")
		return
	else:
		if not DEBUG:
			with open(file_path, 'r') as f: 
				raw_data = re.sub("\n", "", f.read())
		else:
			raw_data = "AAAACCCGGT"

		out = ""
		for i in range(len(raw_data)):
			out += replacer(raw_data[-i-1])
		print(out)

			



if __name__ == "__main__":
	main()
