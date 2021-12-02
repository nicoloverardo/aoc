import pandas as pd

df = pd.read_csv("2021/Day 01/input.txt", header=None, names=["data"])
df["diffs"] = df.data.diff()
df["diff_roll"] = df.data.rolling(window=3).sum().diff()

print(len(df.loc[df.diffs > 0]))
print(len(df.loc[df.diff_roll > 0]))
