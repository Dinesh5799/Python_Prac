import sqlite3

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS COUNTS')

cur.execute('CREATE TABLE COUNTS(email TEXT, count INTEGER)')

fname = input('Enter file name: ')
if len(fname)<=1: fname = 'mbox-short.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '):continue
    pieces = line.split()
    email = pieces[1]
    cur.execute('SELECT count FROM COUNTS WHERE email = ?',(email,))
    row = cur.fetchone()
    #print("row = cur.fetchone() = ",row)
    if row is None:
        cur.execute('INSERT INTO COUNTS(email,count)VALUES(?,1)',(email,))
    else:
        cur.execute('UPDATE COUNTS SET count = count+1 WHERE email = ?',(email,))
    conn.commit()

sqlstr = "SELECT email,count FROM COUNTS ORDER BY count DESC LIMIT 10"

for row in cur.execute(sqlstr):
    print(str(row[0]),row[1])

cur.close()