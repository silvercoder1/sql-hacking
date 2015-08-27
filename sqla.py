import sqlite3, csv

CITIES = [('Boston', 'MA', 600000),
                ('Los Angeles', 'CA', 38000000),
                ('Houston', 'TX', 2100000),
                ('Philadelphia', 'PA', 1500000),
                ('San Antonio', 'TX', 1400000),
                ('San Diego', 'CA', 130000),
                ('Dallas', 'TX', 1200000),
                ('San Jose', 'CA', 900000),
                ('Jacksonville', 'FL', 800000),
                ('Indianapolis', 'IN', 800000),
                ('Austin', 'TX', 800000),
                ('Detroit', 'MI', 700000)]
            
regions = [
            ('New York City', 'Northeast'),
            ('San Francisco', 'West'),
            ('Chicago', 'Midwest'),
            ('Houston', 'South'),
            ('Phoenix', 'West'),
            ('Boston', 'Northeast'),
            ('Los Angeles', 'West'),
            ('Houston', 'South'),
            ('Philadelphia', 'Northeast'),
            ('San Antonio', 'South'),
            ('San Diego', 'West'),
            ('Dallas', 'South'),
            ('San Jose', 'West'),
            ('Jacksonville', 'South'),
            ('Indianapolis', 'Midwest'),
            ('Austin', 'South'),
            ('Detroit', 'Midwest')
             ]


with sqlite3.connect("new.db") as conn:
	cur = conn.cursor()


	'''try:
		
		cur.execute("DROP TABLE IF EXISTS population")
		cur.execute("DROP TABLE IF EXISTS regions")
		cur.execute("CREATE TABLE population(city TEXT, state TEXT, population INT)")
		cur.execute("CREATE TABLE regions(city TEXT, region TEXT)")
	except sqlite3.OperationalError:
		print "table already exists"

	
	try:
		cur.executemany('INSERT INTO population VALUES(?, ?, ?)', CITIES)
		cur.executemany('INSERT INTO regions VALUES(?, ?)', regions)
	except sqlite3.OperationalError as e:
		print "city and/or region data already exists"
		print e'''

	cur.execute('''SELECT DISTINCT population.city, population.population, regions.region FROM 
		population,regions WHERE population.city=regions.city ORDER BY population.city ASC''')
	rows = cur.fetchall()
	for row in rows:
		print row[0], row[1], row[2]





