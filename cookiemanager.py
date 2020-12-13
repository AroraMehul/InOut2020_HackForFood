import os
import pandas as pd 


db = "./pool.csv"

def load_db():
	return pd.read_csv(db)

def save_db(dbf):
	dbf.to_csv(db, index = False)
	return


def create_cookie(id, ck_str):
	dbf = load_db()
	if ( id in dbf['id'].unique() ):
		dbf.loc[dbf['id'] == id, 'uniqueLink'] = ck_str
	else:
		dbf.loc[len(dbf)] = (id, ck_str)

	save_db(dbf)
	return 1

def fetch_cookie(id):
	'''
	error codes
	-2 : id doesn't exist
	'''
	dbf = load_db()
	if ( id in dbf['id'].unique() ):
		return dbf.loc[dbf['id'] == id, 'uniqueLink'].values[0]		
	else:
		return -2

