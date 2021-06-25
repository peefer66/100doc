import pandas as pd

data = pd.read_csv(r'C:\Users\pfiel\Documents\Python\100doc\day 22_30\Day 25 working with csv data and Pandas\Squirrels\Squirrel_data.csv')

fur_color = data.groupby('Primary Fur Color')['Primary Fur Color'].count()
print(fur_color)

