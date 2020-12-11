import os
import pandas as pd 


db = "./pesa_hi_pesa.csv"

def load_db():
	return pd.read_csv(db)

def save_db(dbf):
	dbf.to_csv(db, index = False)
	return


def add_money(user_id, amount):
	dbf = load_db()
	if ( user_id in dbf['user_id'].unique() ):
		dbf.loc[dbf['user_id'] == user_id, 'balance'] += amount
	else:
		dbf.loc[len(dbf)] = (user_id, amount)

	save_db(dbf)
	return

def check_balance(user_id):
	'''
	error codes
	-2 : user doesn't exist
	1 : success
	'''
	dbf = load_db()
	if ( user_id in dbf['user_id'].unique() ):
		return dbf.loc[dbf['user_id'] == user_id, 'balance'].values[0]
		save_db(dbf)
		return 1
	else:
		return -2
	


def deduct_money(user_id, amount):
	'''
	error codes
	-2 : user doesn't exist
	-1 : not enough money
	1 : success
	'''
	
	if(amount > check_balance(user_id)):
		return -1

	dbf = load_db()
	if ( user_id in dbf['user_id'].unique() ):
		dbf.loc[dbf['user_id'] == user_id, 'balance'] -= amount
		save_db(dbf)
		return 1
	else:
		return -2
	

