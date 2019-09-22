import sys
import os
import re

from collections import Counter

def main():
	file_path = sys.argv[1]
	if file_path[:2] != "./" and file_path[0] != "/" and file_path[:3] != "../" and file_path not in os.listdir():
		print("Fatal error: path not understood!")
		return
	else:
		with open(file_path, 'r') as f: 
			raw_data = f.read()
		counts = Counter(raw_data)
		print(counts["A"], counts["C"], counts["G"], counts["T"])


if __name__ == "__main__":
	main()
