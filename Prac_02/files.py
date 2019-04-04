OUTPUT_FILE = "name.txt"

out_file = open(OUTPUT_FILE, 'w')

name = input("Your name: ")
print("Your name is {}".format(name), file=out_file)

out_file.close()
