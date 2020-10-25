#9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. 
#The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. 
#The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. 
#After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"#if lenght of name is less then one then show name = mbox-short.txt
handle = open(name)#if it is more then one then open the file using a handle
mailname = dict()#declaring a dictionaries as "mailname"
for B1 in handle :
    if B1.startswith("From "): 
        L1 = B1.split()#if line startswith "From:" then split them
        #print(L1)
        W2 = L1[1]# From the "From:" line take 2nd word and store it in "W2"
        #print(W2)
        mailname[W2] = mailname.get(W2, 0) + 1#count the number of times each key appears

wrd = None
val = None

for a, b in mailname.items():
    if val is None or val < b:
        wrd = a
        val = b
print(wrd,val)            
