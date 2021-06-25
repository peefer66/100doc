import pandas as pd

student_dict = {
    "student":['Peter', 'Karen','Mollie'],
    "score":[54,84,26]
    }

student_df = pd.DataFrame(student_dict)
print(student_df)

#loop through the dataframe as you would a dictionary

# for key,value in student_df.items():
#     print(key,value)

# Pandas as an inbuilt looping function itterows()

for (index,row) in student_df.iterrows():
    print(row.score)