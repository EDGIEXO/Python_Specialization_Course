import sqlite3

conn = sqlite3.connect('emailassignmentdb.sqlite')
handle = conn.cursor()

handle.execute('DROP TABLE IF EXISTS Counts')

handle.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
    email1 = pieces[1]
    email = email1.split("@")
    org = email[1]
    handle.execute('SELECT count FROM Counts WHERE org = ? ', (org,))
    row = handle.fetchone()
    #print(row)
    if row is None:
        handle.execute('''INSERT INTO Counts (org, count)
                VALUES (?, 1)''', (org,))
    else:
        handle.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
                    (org,))
conn.commit()

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in handle.execute(sqlstr):
    print(str(row[0]), row[1])

handle.close()
