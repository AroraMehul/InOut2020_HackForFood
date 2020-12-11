import pandas as pd
import numpy as np
import math

def create_pool(subscript, p1, p2, p3, p4, leader):

	pool_db_file = "pool.csv"
	pool_db = pd.read_csv(pool_db_file)

	row = {"id" : int(max(list(pool_db["id"])) + 1), "subscription" : str(subscript), "domain" : None, "uniqueLink" : None, "startDate" : None, "duration" : None, "status" : None, "p1" : p1, "p2" : p2, "p3" : p3, "p4" : p4, "leader" : leader}
	#row = pd.DataFrame.from_dict(row)
	pool_db = pool_db.append(row, ignore_index=True)

	if("Unnamed: 0" in pool_db.columns):
		pool_db = pool_db.drop(["Unnamed: 0"], axis=1)
	pool_db.to_csv("pool.csv")
	print(pool_db, "\nDone")

def join_pool(subscript, p1):

	pool_db_file = "pool.csv"
	pool_db = pd.read_csv(pool_db_file)

	pool_db_sub = pool_db.loc[pool_db["subscription"] == subscript]
	col = None
	uid = -1
	for idx, row in pool_db_sub.iterrows():
		#print(math.isnan(float(row["p3"])), row["p4"])
		if(math.isnan(float(row["p1"]))):
			col = "p1"
		elif math.isnan(float(row["p2"])) :
			col = "p2"
		elif math.isnan(float(row["p3"])):
			col = "p3"
		elif math.isnan(float(row["p4"])) :
			col = "p4"
		else:
			col = None

		if(col is not None):
			uid = row["id"]
			break

	if(col is not None):
		pool_db.loc[pool_db["id"] == uid, col] = p1

		if("Unnamed: 0" in pool_db.columns):
				pool_db = pool_db.drop(["Unnamed: 0"], axis=1)

		print(pool_db)
		pool_db.to_csv("pool.csv")

	else:
		print("No empty pool available, creating new pool ...")
		create_pool(subscript, p1, None, None, None, p1)
		print("Pool created")

join_pool("Netflix", "5")