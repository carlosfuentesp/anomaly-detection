from source.adquire_data import read_data
from source.preprocess import process
from source.train import train
from source.validate import validate


def run():
    df = read_data()
    x_normal, x_attack = process(df)
    model, x_normal_test = train(x_normal)
    validate(model, x_normal, x_attack, x_normal_test)
