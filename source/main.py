from source.machine_learning.adquire_data import read_data
from source.machine_learning.preprocess import process
from source.machine_learning.train import train
from source.machine_learning.validate import validate
from source.ingestion.download_file import get_file
from cd4ml import tracking
from cd4ml.pipeline_params import pipeline_params


def run():
    get_file()

    df = read_data()
    x_normal, x_attack = process(df)

    model_name = pipeline_params['model_name']
    params = pipeline_params['model_params'][model_name]

    with tracking.track() as track:
        model, x_normal_test = train(x_normal, params)
        track.log_ml_params(params)
        track.log_pipeline_params(pipeline_params)
        validate(model, x_normal, x_attack, x_normal_test, track)
