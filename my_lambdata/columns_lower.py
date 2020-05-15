# Function to put all columns in lower case
def lower(dataframe):
    print('df before:', dataframe.head())
    dataframe.columns = map(str.lower, dataframe.columns)
    print('dataframe after:', dataframe.head())
    return dataframe