import pandas as pd
import numpy as np

automobile_data = pd.read_csv('E:/Downloads/Lab 2 Bilyi/Automobile_data.csv')

#----------------------------------------------------------------------------------------------------------------------------
"""From the given data set print the first and last five rows"""

print(automobile_data.head())
print(automobile_data.tail())


#----------------------------------------------------------------------------------------------------------------------------
"""Clean data and update the CSV file (Replace all column values which contain ‘?’ and n.a with NaN.)"""

automobile_data[automobile_data[:] == '?'] = np.NaN
print(automobile_data.head(30))



#----------------------------------------------------------------------------------------------------------------------------
"""Find the most expensive car company name"""

automobile_data['price'] = automobile_data['price'].astype(float)

print(automobile_data.loc[automobile_data['price']==automobile_data['price'].max(),'make'])


#----------------------------------------------------------------------------------------------------------------------------
"""Print All Toyota Cars details"""

print(automobile_data.loc[automobile_data['make'] == 'toyota'])


#----------------------------------------------------------------------------------------------------------------------------
"""Count total car per company"""

list_of_unique_value = automobile_data['make'].unique()
for company in list_of_unique_value:
    print(company,':',automobile_data.loc[automobile_data['make'] == company,'make'].count())


#----------------------------------------------------------------------------------------------------------------------------
"""Find each company’s Highest price car"""

for company in list_of_unique_value:
    print(company,':',automobile_data.loc[automobile_data['make'] == company,'price'].max())


#----------------------------------------------------------------------------------------------------------------------------
"""Find the average mileage of each car making company"""

both_mileage = automobile_data[['city-mpg','highway-mpg']].mean(axis=1)
cars_name = automobile_data['make']

automobile_data_with_name_mileages = pd.DataFrame({'make':cars_name,'mileage':both_mileage})

print(automobile_data_with_name_mileages.groupby('make')['mileage'].mean())


#----------------------------------------------------------------------------------------------------------------------------
"""Sort all cars by Price column"""

automobile_data = automobile_data.sort_values(by=['price'],ascending=False)
print(automobile_data)
