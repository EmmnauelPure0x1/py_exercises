# Reading from a text file

print("++++++++++")

text = open('text.txt', 'r')

for line in text:
    print(line.title())

text.close()

print("++++++++++")