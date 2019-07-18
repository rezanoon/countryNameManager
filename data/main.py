import pandas as pd

d = pd.read_csv('export.csv', sep=';')
d2 = d.drop([0], axis=1)
d2.to_csv('sample.csv')
