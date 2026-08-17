import pandas as pd

student = {"Name": ["Rose", "John", "James"], "Age": [25, 30, 38]}
df = pd.DataFrame(student)
print(df)
print(type(df))
print(df["Name"])


print(type(df))
print(type(df["Name"]))
print(type(df[["Name"]]))