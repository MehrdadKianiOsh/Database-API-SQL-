import pandas as pd

df=pd.read_csv("gapminder.csv")

print(df)

print(df[df["country"].str.contains(r"^[BDC]")])

df["short"]=df["country"].str.extract(r"^([a-zA-Z]{4})")

print(df)