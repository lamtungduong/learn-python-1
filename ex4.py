from sys import argv

script, filename = argv

print "We are going to erase %r." % filename
raw_input("?")

print "Opening the file ...."
target = open(filename, 'w')
print "three lines"
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "write"
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "close"
target.close()