import model, sqlite3

options = """1. Average
2. Max
3. Min
4. Sum
5. Exit\n"""

sql = {1: 'SELECT avg(numbers) from randnum',
2: 'SELECT max(numbers) from randnum',
3: 'SELECT min(numbers) from randnum',
4: 'SELECT sum(numbers) from randnum'}

def get_choice():
	print options
	choice = raw_input("Choose what you wanna do: ")
	return choice



while True:
	
	choice = get_choice()
	try:
		int(choice)
	except:
		print "Enter an integer corresponding to the options\n"
		choice = get_choice()
	choice = int(choice)
	if choice == 5:
		print "Exiting now..\n"
		break
	elif choice < 1 or choice > 5:
		print "Enter integer between 1 and 5\n"
		continue
	else:
		with sqlite3.connect("newnum.db") as conn:
			cur = conn.cursor()
			cur.execute(sql[choice])
			print str(cur.fetchone()[0]) + "\n\n"



