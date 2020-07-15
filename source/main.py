from source.reader import read_data
from source.preprocess import process


def run():
    df = read_data()
    df = process(df)
    print(df.head())
