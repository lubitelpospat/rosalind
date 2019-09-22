import sys
import os
import re

from collections import Counter
def replacer(letter):
	if letter == "T":
		return "U"
	else:
		return letter



def main():
	file_path = sys.argv[1]
	if file_path[:2] != "./" and file_path[0] != "/" and file_path[:3] != "../" and file_path not in os.listdir():
		print("Fatal error: path not understood!")
		return
	else:
		with open(file_path, 'r') as f: 
			raw_data = re.sub("\n", "", f.read())
		out = ""
		for i in range(len(raw_data)):
			out += replacer(raw_data[i])
		print(out)

			


if __name__ == "__main__":
	main()
