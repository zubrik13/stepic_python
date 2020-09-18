#! /bin/bash/python

inp = int(input())
# inp = 113

space_range = list(range(1001))

if inp in space_range:

	n = str(inp)

	if n == "1":
		print(f"{inp} программист")

	elif (len(n) > 1) and (n[-2] != "1") and n[-1] == "1":
		print(f"{inp} программист")

	elif (len(n) == 1) and ((n[-1] == "2") or (n[-1] == "3") or (n[-1] == "4")):
		print(f"{inp} программиста")
		print()

	elif ((len(n) > 1) and (n[-2] != "1")) and ((n[-1] == "2") or (n[-1] == "3") or (n[-1] == "4")):
		print(f"{inp} программиста")

	elif (len(n) > 1) and (n[-2:] == "11"):
		print(f"{inp} программистов")

	elif (len(n) > 1) and (n[-2:] == "12") or (n[-2:] == "13") or (n[-2:] == "14"):
		print(f"{inp} программистов")

	else:
		print(f"{inp} программистов")

else:
	print(f"{inp} is out of range")


