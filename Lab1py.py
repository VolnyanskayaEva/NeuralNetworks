import pandas as pd
#task read
d1=  pd.read_table('E:/Downloads/Lab 1 Bilyi/ml-1m/users.dat', engine='python', delimiter = '::', names=['UserId', 'Gender', 'Age', 'Occupation', 'fd'])
d2= pd.read_table('E:/Downloads/Lab 1 Bilyi/ml-1m/ratings.dat',engine='python',  delimiter = '::', names=['UserId', 'MovieId', 'Rat', 'Time'])
d3= pd.read_table('E:/Downloads/Lab 1 Bilyi/ml-1m/movies.dat', engine='python', delimiter = '::', names=['MovieId', 'Title', 'Genre'])

user = pd.DataFrame(d1)
rating = pd.DataFrame(d2)
movie = pd.DataFrame(d3)

#task merge
#merged = pd.merge(user,rating,on='UserId')
#print(merged.to_string())
merged = pd.merge(pd.merge(user,rating,on='UserId'),movie,on='MovieId')
#print(merged.sort_values(by=['MovieId']).to_string())
#task group
merged.loc[merged['Age'].between(0, 25), 'Age_range'] = 1
merged.loc[merged['Age'].between(25, 40), 'Age_range'] = 2
merged.loc[merged['Age'].between(40, 50), 'Age_range'] = 3
merged.loc[merged['Age'].between(50, 60), 'Age_range'] = 4

#gr = merged.groupby(['Age_range'],sort=True).head()

#print(gr)
#for _, a in merged.groupby(['Age_range']): print('#####Next age range#####\n', a.to_string())


#Task sort
print('Task sort')

#sort = merged.sort_values(by=['Rat', 'MovieId']).groupby(['Gender', 'Age_range'])
#print(sort.head())

for _, a in merged.sort_values(['Rat']).groupby(['Gender','Age_range']): print('#####Next age range#####\n', a.head(10).to_string())
