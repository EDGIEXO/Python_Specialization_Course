#10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. 
#You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
timer = dict()
sorting = []
for line1 in handle :
    if not line1.startswith("From") : continue#if line does not start with "From" continue
    word = line1.split()#split each line
    if len(word) < 4 : continue#if length of the word is less then four continue
    time_clock = word[5]#take the 5 index sequence and place it in time_clock
    time_clock = time_clock.split(':')#split(:)
    hour_clock = time_clock
    #print(hour_clock)
    for time in hour_clock[0:1] :
        timer[time] = timer.get(time ,0) + 1
#print(timer)
#sorting=sorted([(a,b) for a,b in timer.items()],reverse=True)
for a,b in timer.items():
    sorting.append((a,b))#for items in timer append them to "sorting" list 
    sorting.sort()#sort the list
#print(sorting)    
for a1,b1 in sorting:
   print (a1,b1)