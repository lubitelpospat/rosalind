
import sys
import os


def main():
	__doc__  = """
	F_n = F_(n-1) + k*F_(n-2)
	




			"""

	n, k = int(sys.argv[1]),int(sys.argv[2])
	Fimo = 1
	Fimt = 1
	F = 0
	for i in range(2, n):
		Fimo, Fimt = Fimo + k * Fimt, Fimo
	print(Fimo)

if __name__ == "__main__":
	main()