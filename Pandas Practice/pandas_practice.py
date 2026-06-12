import pandas as pd

data = {
    "names":['Kofi', 'Yaa', 'Yaw','Fii','Kwame','Kwesi', 'Afia'],
    'age':[12,4,55,6,1,'',8],
    'class':[1,3,1,4,3,2,4]
}

df = pd.DataFrame(data)

# print(df)
# print(data)

df2 = [1,2,3]

# print(df2)

df3 = pd.Series(df2, index = ['a','b','c'])

# print(df3)

# print(df3['b'])

# print(df.loc[[0,1,3]])

w3_data = pd.read_csv("./Data/data.csv")

print(w3_data)

print(pd.options.display.max_rows)
