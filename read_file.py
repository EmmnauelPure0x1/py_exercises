# Reading from a text file
'''
print("++++++++++")

# opening text document and adding 'read' powers. Storing this action into text variable
text = open('text.txt', 'r')

# looping over each line in the text file and printing it capitalized.
for line in text:
    print(line.title())

# var which equals opened document is closed (best practice)
text.close()

print("++++++++++")
'''
t2 = open('text_file_2.txt')

for char in t2.readlines():
    for i in char:
        print(i)

t2.close()

