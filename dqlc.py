import sqlite3

with sqlite3.connect("new.db") as conn:
	cur = conn.cursor()

	sql = {'average': 'SELECT avg(population) FROM population',
	'maximum': 'SELECT max(population) from population',
	'minimum': 'SELECT min(population) FROM population',
	'sum': 'SELECT sum(population) FROM population',
	'count': 'SELECT count(population) FROM population'}

	for key, value in sql.iteritems():

		cur.execute(value)
		row = cur.fetchone()

		print key + ":" + str(row[0])
