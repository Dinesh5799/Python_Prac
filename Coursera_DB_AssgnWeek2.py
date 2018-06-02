import sqlite3

conn = sqlite3.connect('email2db.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('CREATE TABLE Counts(org TEXT,count INTEGER)')

fname = input('Enter file name: ')
if len(fname)<1:fname = 'mbox.txt'
fn = open(fname)
for line in fn:
    if line.startswith('From '):
        pi = line.split()
        email = pi[1]
        email = email.split('@')
        org = email[1]
        #print("org = ",org)
        cur.execute('SELECT count FROM Counts WHERE org = ?',(org,))
        row = cur.fetchone()
        if row is None:
            cur.execute('INSERT INTO Counts(org,count)VALUES(?,1)',(org,))
        else:
            cur.execute('UPDATE Counts SET count = count+1 Where org = ?',(org,))
conn.commit()

sqlstr = 'SELECT org,count FROM Counts ORDER BY count'

for ha in cur.execute(sqlstr):
    print(str(ha[0]),ha[1])
cur.close()