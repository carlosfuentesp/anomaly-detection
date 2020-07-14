from source.reader import read_data
from source.preprocess import process


df = read_data()
df = process(df)
print(df.head())