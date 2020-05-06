import pandas
from my_lambdata.my_mod import enlarge

print('Hello World')

df = pandas.DataFrame({'state':['CT', 'CO', 'CA', 'CA', 'TX']})
print(df.head())

print("--------------")

x = 11
print('Number', x)
print('Enlarged number', enlarge(x)) #invoking the function