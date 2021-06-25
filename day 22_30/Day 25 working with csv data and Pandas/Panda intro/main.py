# import csv

# with open(r'day 22_30\Day 25 working with csv data and Pandas\Reading CSV\weather_data.csv') as data_file:
#     data = csv.reader(data_file)
#     for row in data:
#         temperature = [int(row[1]) for row in data]
#     print(temperature)

import pandas as pd
from statistics import mean
data = pd.read_csv(r'C:\Users\pfiel\Documents\Python\100doc\day 22_30\Day 25 working with csv data and Pandas\Reading CSV\weather_data.csv')

# #print(data)
# #print(data['temp'])
# data_dict = data.to_dict()
# print(data_dict)
# temp_list = data['temp'].to_list()
# print(temp_list)
# average_temp = data['temp'].mean()
# print(average_temp)
# print()
# maximum = data['temp'].max()
# print('Max Value = ',maximum)
# print(data['condition'])
# # OR
# print(data.condition)

# Get Row data
# print(data[data.day == 'Monday'])

# print(data[data.temp == data.temp.max()])

# monday = data[data.day == 'Monday']
# print(monday.condition)

# print(monday.temp * (9/5)+32) 

data_dict = {'students':['Peter','Karen','Mollie'], 'grades':[80,98,56]}
data = pd.DataFrame(data_dict)
print(data)
data.to_csv(r'C:\Users\pfiel\Documents\Python\100doc\day 22_30\Day 25 working with csv data and Pandas\new_data.csv')

