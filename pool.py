import pandas as pd

def create_pool(subscript, p1, p2, p3, p4, leader):

	pool_db_file = "pool.csv"
	pool_db = pd.read_csv(pool_db_file)

	row = [{"id" : int(max(list(pool_db["id"])) + 1), "subscription" : str(subscript), "domain" : None, "uniqueLink" : None, "startDate" : None, "duration" : None, "status" : None, "p1" : p1, "p2" : p2, "p3" : p3, "p4" : p4, "leader" : leader}]
	row = pd.DataFrame.from_dict(row)
	pool_db.append(row)

	#pool_db.to_csv("pool.csv")
	print(pool_db, "\nDone")

create_pool("Netflix", "1", "2", "3", "4", "1")