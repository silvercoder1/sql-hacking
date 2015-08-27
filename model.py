import sqlite3, random

with sqlite3.connect("newnum.db") as conn:
	cur = conn.cursor()
	cur.execute('''DROP table if exists randnum''')
	cur.execute('''CREATE table randnum(numbers INT)''')
	numbers = []
	for i in range (0, 100):
		numbers.append(random.randint(0, 100))
		cur.execute('INSERT INTO randnum VALUES(?)', (random.randint(0, 100),))