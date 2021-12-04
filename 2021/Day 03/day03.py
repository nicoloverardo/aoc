import pandas as pd

with open("input.txt", "r") as f:
    lines = f.readlines()

lines = [list(line.replace("\n", "")) for line in lines]
df = pd.DataFrame(lines, columns=["bit" + str(i) for i in range(len(lines[0]))])

# Part 1
df1 = df.T.copy(deep=True)
df1["gamma"] = df1.apply(lambda x: x.mode(), axis=1)
df1["epsilon"] = df1.gamma.replace({"0": "1", "1": "0"})

print(int(df1.gamma.sum(), base=2) * int(df1.epsilon.sum(), base=2))

# Part 2
def compute_max(df, col, typ="oxy"):
	if len(df[col].mode().values) == 2:
		if typ == "oxy":
			return "1"
		elif typ == "co2":
			return "0"
		else:
			raise ValueError("Type not found.")
	else:
		if typ == "oxy":
			return df[col].mode().values[0]
		else:
			return str(1 - int(df[col].mode().values[0]))

def compute_decimal(df, typ="oxy"):
	i = 0
	stop = False
	df_tmp = df.copy(deep=True)
	
	while not stop:
		df_tmp = df_tmp.loc[
            df_tmp[df_tmp.columns[i]] == compute_max(df_tmp, df_tmp.columns[i], typ=typ)
        ]

		i += 1

		if df_tmp.shape[0] == 1:
			stop = True

	return int(df_tmp.sum().sum(), base=2)

print(compute_decimal(df, typ="oxy") * compute_decimal(df, typ="co2"))
