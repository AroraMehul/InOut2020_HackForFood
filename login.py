import pandas as pd

def login(username, password):

	user_file = "user.csv"
	user_db = pd.read_csv(user_file)

	if username not in list(user_db["email"]):
		return "email not found"

	else:
		row = user_db.loc[user_db["email"] == username]
		if not row["password"].tolist()[0] == password :
			return "wrong password"
		else :
			print(user_db.loc[user_db["email"] == username])
			return "login success"

def signup(username, password):

	user_file = "user.csv"
	user_db = pd.read_csv(user_file)

	row = {"email" : str(username), "password" : str(password), "isLeader" : 0, "pool" : 0, "uid" : int(max(list(user_db["uid"])) + 1)}
	user_db = user_db.append(row,ignore_index=True)

	if("Unnamed: 0" in user_db.columns):
		user_db = user_db.drop(["Unnamed: 0"], axis=1)
	user_db.to_csv("user.csv")
	print(user_db, "\nDone")

signup("test8", "test0")
