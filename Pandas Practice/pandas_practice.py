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

# print(w3_data)

# print(pd.options.display.max_rows)

json_data = pd.read_json('./Data/data.json')

# print(json_data.to_string())

# Cleaning data

# new_df = json_data.dropna()
# print(json_data.info())
print(json_data.to_string())

# print('1-----------------------------------')

# print(new_df)
# print(new_df.isnull().sum())
# print(new_df.info())


# print('2-----------------------------------')
# new_df2 = json_data.fillna(130)

# print(new_df2.to_string())

# # to replace a specific column it will be new_df2.fillna({'Calories':130})
# print('3-----------------------------------')


# print(new_df2['Calories'].mean())


print('4-----------------------------------')


new_data = [
    {'Duration': 60, 'Date': '2020/12/01', 'Pulse': 110, 'Maxpulse': 130, 'Calories': 409.1},
    {'Duration': 60, 'Date': '2020/12/02', 'Pulse': 117, 'Maxpulse': 145, 'Calories': 479.0},
    {'Duration': 60, 'Date': '2020/12/03', 'Pulse': 103, 'Maxpulse': 135, 'Calories': 340.0},
    {'Duration': 45, 'Date': '2020/12/04', 'Pulse': 109, 'Maxpulse': 175, 'Calories': 282.4},
    {'Duration': 45, 'Date': '2020/12/05', 'Pulse': 117, 'Maxpulse': 148, 'Calories': 406.0},
    {'Duration': 60, 'Date': '2020/12/06', 'Pulse': 102, 'Maxpulse': 127, 'Calories': 300.0},
    {'Duration': 60, 'Date': '2020/12/07', 'Pulse': 110, 'Maxpulse': 136, 'Calories': 374.0},
    {'Duration': 450, 'Date': '2020/12/08', 'Pulse': 104, 'Maxpulse': 134, 'Calories': 253.3},
    {'Duration': 30, 'Date': '2020/12/09', 'Pulse': 109, 'Maxpulse': 133, 'Calories': 195.1},
    {'Duration': 60, 'Date': '2020/12/10', 'Pulse': 98, 'Maxpulse': 124, 'Calories': 269.0},
    {'Duration': 60, 'Date': '2020/12/11', 'Pulse': 103, 'Maxpulse': 147, 'Calories': 329.3},
    {'Duration': 60, 'Date': '2020/12/12', 'Pulse': 100, 'Maxpulse': 120, 'Calories': 250.7},
    {'Duration': 60, 'Date': '2020/12/12', 'Pulse': 100, 'Maxpulse': 120, 'Calories': 250.7},
    {'Duration': 60, 'Date': '2020/12/13', 'Pulse': 106, 'Maxpulse': 128, 'Calories': 345.3},
    {'Duration': 60, 'Date': '2020/12/14', 'Pulse': 104, 'Maxpulse': 132, 'Calories': 379.3},
    {'Duration': 60, 'Date': '2020/12/15', 'Pulse': 98, 'Maxpulse': 123, 'Calories': 275.0},
    {'Duration': 60, 'Date': '2020/12/16', 'Pulse': 98, 'Maxpulse': 120, 'Calories': 215.2},
    {'Duration': 60, 'Date': '2020/12/17', 'Pulse': 100, 'Maxpulse': 120, 'Calories': 300.0},
    {'Duration': 45, 'Date': '2020/12/18', 'Pulse': 90, 'Maxpulse': 112, 'Calories': None},
    {'Duration': 60, 'Date': '2020/12/19', 'Pulse': 103, 'Maxpulse': 123, 'Calories': 323.0},
    {'Duration': 45, 'Date': '2020/12/20', 'Pulse': 97, 'Maxpulse': 125, 'Calories': 243.0},
    {'Duration': 60, 'Date': '2020/12/21', 'Pulse': 108, 'Maxpulse': 131, 'Calories': 364.2},
    {'Duration': 45, 'Date': None, 'Pulse': 100, 'Maxpulse': 119, 'Calories': 282.0},
    {'Duration': 60, 'Date': '2020/12/23', 'Pulse': 130, 'Maxpulse': 101, 'Calories': 300.0},
    {'Duration': 45, 'Date': '2020/12/24', 'Pulse': 105, 'Maxpulse': 132, 'Calories': 246.0},
    {'Duration': 60, 'Date': '2020/12/25', 'Pulse': 102, 'Maxpulse': 126, 'Calories': 334.5},
    {'Duration': 60, 'Date': '20201226', 'Pulse': 100, 'Maxpulse': 120, 'Calories': 250.0},
    {'Duration': 60, 'Date': '2020/12/27', 'Pulse': 92, 'Maxpulse': 118, 'Calories': 241.0},
    {'Duration': 60, 'Date': '2020/12/28', 'Pulse': 103, 'Maxpulse': 132, 'Calories': None},
    {'Duration': 60, 'Date': '2020/12/29', 'Pulse': 100, 'Maxpulse': 132, 'Calories': 280.0},
    {'Duration': 60, 'Date': '2020/12/30', 'Pulse': 102, 'Maxpulse': 129, 'Calories': 380.3},
    {'Duration': 60, 'Date': '2020/12/31', 'Pulse': 92, 'Maxpulse': 115, 'Calories': 243.0}
]
new_data = pd.DataFrame(new_data)
print(new_data)