import sqlite3, csv

CITIES = [('Mumbai', 'Maharashatra', 3200000),
('New Delhi', 'NCR', 1900000),
('Bengaluru(Bangalore)', 'Karnataka', 800000),
('Chennai', 'TN', 1500000),
('Jaipur', 'Rajasthan', 7000000),
('Shimla', 'Himachal Pradesh', 2000000)]

'''with sqlite3.connect("new.db") as conn:
	cur = conn.cursor()


	try:
		cur.execute("CREATE TABLE employees(firstname TEXT, lastname TEXT)")
		cur.execute("CREATE TABLE population(city TEXT, state TEXT, population INT)")
	except sqlite3.OperationalError:
		print "table already exists"

	employees = csv.reader(open("employees.csv", "rU"))
	cur.executemany('INSERT INTO employees VALUES(?, ?)', employees)

	try:


		cur.execute("INSERT INTO population VALUES('New York City', 'NY', 22000000)")
		cur.execute("INSERT INTO population VALUES('Los Angeles', 'CA', 4034113)")
	except sqlite3.OperationalError:
		print "initial city data already exists"

	
	try:
		cur.executemany('INSERT INTO population VALUES(?, ?, ?)', CITIES)
	except sqlite3.OperationalError as e:
		print "list city data already exists"
		print e'''


CARS = [('Ford', 'Countach 1.2', 10000),
('Ford', 'Focus', 27221),
('Ford', 'BroGap22', 1900),
('Honda', 'Civic 2001', 125000),
('Honda', 'City', 19000)]


with sqlite3.connect("cars.db") as conn:
	cur = conn.cursor()
	'''try:
		cur.execute("DROP TABLE IF EXISTS inventory")
		cur.execute("CREATE TABLE inventory(make TEXT, model TEXT, quantity INT)")
		cur.executemany('INSERT INTO inventory VALUES(?, ?, ?)', CARS)
	except sqlite3.OperationalError:
		print "car inventory table already exists"

	cur.execute("UPDATE inventory SET quantity=12512 WHERE model='Civic 2001'")
	cur.execute("UPDATE inventory SET quantity=20000 WHERE model='Focus'")'''

	for row in cur.execute("SELECT * FROM inventory WHERE make='Ford'"):
		print row[0], row[1], row[2]


