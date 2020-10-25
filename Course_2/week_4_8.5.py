#8.5 Open the file mbox-short.txt and read it line by line. 
#When you find a line that starts with 'From ' like the following line:
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#You will parse the From line using split() and print out the second word in the line (i.e. the entire address of the person who sent the message). Then print out a count at the end.
#Hint: make sure not to include the lines that start with 'From:'.

#You can download the sample data at http://www.py4e.com/code3/mbox-short.txt

filename = input("enter the file name:")
filehandler = open(filename)
count = 0
for l in filehandler :
    if l.startswith("From:"):
        a1 = l.split()
        print(a1[1])
        count = count + 1     
print("There were", count, "lines in the file with From as the first word")
