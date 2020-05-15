# Train/validate/test split for a dataframe
from sklearn.model_selection import train_test_split

def tt_split(df, tr, ts, rs):
    train, val = train_test_split(df, train_size=tr, test_size=ts, random_state=rs)
    return train, val
