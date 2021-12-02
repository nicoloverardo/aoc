import pandas as pd

df = pd.read_csv("2021/Day 02/input.txt", sep=" ", header=None, names=["move", "val"])

# Part 1
df.loc[df.move == "up", "val"] *= -1
df.move = df.move.replace({"down": "depth", "up": "depth"})
dfg = df.groupby("move").agg({"val": sum})
print(dfg.val["depth"] * dfg.val["forward"])

# Part 2
# Cumsum helps us to avoid a for loop.
df["aim"] = df[df.move == "depth"]["val"].cumsum()
df["hor"] = df[df.move == "forward"]["val"].cumsum()
df.aim = df.aim.fillna(method="ffill").fillna(0)
df.hor = df.hor.fillna(method="ffill")
df["d"] = (df[df.move == "forward"]["val"] * df[df.move == "forward"]["aim"]).cumsum()
print(df.iloc[-1].hor * df.iloc[-1].d)
