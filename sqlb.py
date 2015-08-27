import sqlite3

CARS = [('Ford', 'Countach 1.2', 10000),
('Ford', 'Focus', 27221),
('Ford', 'BroGap22', 1900),
('Honda', 'Civic 2001', 125000),
('Honda', 'City', 19000)]

ORDERS = [('Ford', 'Countach 1.2', '1991-09-22'),
('Ford', 'Countach 1.2', '1961-04-12'),
('Ford', 'Countach 1.2', '1992-01-02'),
('Ford', 'Focus', '2007-11-30'),
('Ford', 'Focus', '2013-12-20'),
('Ford', 'Focus', '2008-07-19'),
('Ford', 'BroGap22', '2001-01-30'),
('Ford', 'BroGap22', '2000-01-01'),
('Ford', 'BroGap22', '2007-10-07'),
('Honda', 'Civic 2001', '2001-05-10'),
('Honda', 'Civic 2001', '2001-06-29'),
('Honda', 'Civic 2001', '1999-01-30'),
('Honda', 'City', '1994-03-31'),
('Honda', 'City', '2014-08-15'),
('Honda', 'City', '2012-05-03')]


with sqlite3.connect("cars.db") as conn:
	cur = conn.cursor()
	try:
		cur.execute("DROP TABLE IF EXISTS inventory")
		cur.execute("DROP TABLE IF EXISTS orders")
		cur.execute("CREATE TABLE inventory(make TEXT, model TEXT, quantity INT)")
		cur.execute("CREATE TABLE orders(make TEXT, model TEXT, order_date DATE)")
		cur.executemany('INSERT INTO inventory VALUES(?, ?, ?)', CARS)
		cur.executemany('INSERT INTO orders VALUES(?, ?, ?)', ORDERS)
	except sqlite3.OperationalError:
		print "car inventory table already exists"

	cur.execute("UPDATE inventory SET quantity=12512 WHERE model='Civic 2001'")
	cur.execute("UPDATE inventory SET quantity=20000 WHERE model='Focus'")

	cur.execute('''SELECT * from inventory''')
	rows = cur.fetchall()

	
	for row in rows:
		cur.execute('''SELECT orders.order_date FROM orders WHERE orders.make=? AND orders.model=?''', (row[0], row[1]))
		brows = cur.fetchall()
		print "Car: ", row[0], row[1]
		print "Quantity: ", row[2]
		print "Order Dates: ", ", ".join([dt[0] for dt in brows])
		cur.execute('''SELECT count(orders.order_date) from orders
		 WHERE orders.make=? AND orders.model=?''', (row[0], row[1]))
		print "Total Orders: {}\n".format(cur.fetchone()[0])

	
