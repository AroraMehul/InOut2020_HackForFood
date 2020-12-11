import pandas as pd
import numpy as np
import math

def create_pool(p1, subscript, startDate, duration):

	pool_db_file = "pool.csv"
	pool_db = pd.read_csv(pool_db_file)

	row = {"id" : int(max(list(pool_db["id"])) + 1), "subscription" : str(subscript), "domain" : None, "uniqueLink" : None, "startDate" : startDate, "duration" : duration, "status" : None, "p1" : p1, "p2" : None, "p3" : None, "p4" : None, "leader" : p1}
	pool_db = pool_db.append(row, ignore_index=True)

	if("Unnamed: 0" in pool_db.columns):
		pool_db = pool_db.drop(["Unnamed: 0"], axis=1)
	pool_db.to_csv("pool.csv")
	print(pool_db, "\nDone")

def join_pool(uid, p1):

	pool_db_file = "pool.csv"
	pool_db = pd.read_csv(pool_db_file)

	col = None

	row = pool_db.loc[pool_db["id"] == uid]

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
		pool_db.loc[pool_db["id"] == uid, col] = p1

		if("Unnamed: 0" in pool_db.columns):
				pool_db = pool_db.drop(["Unnamed: 0"], axis=1)

		print(pool_db)
		pool_db.to_csv("pool.csv")
	else:
		print("No available spaces in pool")

create_pool(10, "Netflix", "10-10-2020", 4)