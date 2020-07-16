from source.adquire_data import read_data
from source.preprocess import process
from source.train import train
from source.validate import validate
from cd4ml import tracking
from cd4ml.pipeline_params import pipeline_params


def run():
    df = read_data()
    x_normal, x_attack = process(df)

    model_name = pipeline_params['model_name']
    params = pipeline_params['model_params'][model_name]

    with tracking.track() as track:
        model, x_normal_test = train(x_normal, params)
        track.log_ml_params(params)
        track.log_pipeline_params(pipeline_params)
        validate(model, x_normal, x_attack, x_normal_test, track)
