import sqlite3

with sqlite3.connect('cars.db') as conn:
	cur = conn.cursor()
	cur.execute('select count(orders.order_date) ')