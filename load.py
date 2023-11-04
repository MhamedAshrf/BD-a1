import pandas as pd
import sys
def p():
    path = sys.argv[1]
    data = pd.read_csv(path)
    return data
