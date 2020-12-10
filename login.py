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