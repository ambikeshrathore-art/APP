file1 = open("input.txt", "r")

L = file1.readlines()

print("Total number of lines:", len(L))

L = L[:2]

file1.close()

file2 = open("output.txt", "w")

file2.writelines(L)

file2.close()

print("Extracted lines written to output.txt")
