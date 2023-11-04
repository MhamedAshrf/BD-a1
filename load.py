import pandas as pd
def p():
    path = input("Please Enter the Path of the dataset: ")
    data = pd.read_csv(path)
    return data
