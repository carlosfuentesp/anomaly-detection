from sklearn import metrics
import numpy as np
import json
import os
from cd4ml.filenames import file_names


def write_predictions_and_score(evaluation_metrics):
    filename = 'results/metrics.json'
    print("Writing to {}".format(filename))
    if not os.path.exists('results'):
        os.makedirs('results')
    with open(filename, 'w+') as score_file:
        json.dump(evaluation_metrics, score_file)


def write_model(model):
    filename = file_names['model']
    print("Writing to {}".format(filename))
    # FIX Unable to create file (unable to open file: name = 'data/models/', errno = 21,
    # error message = 'Is a directory', flags = 13, o_flags = 242)
    # model.save(filename)


def validate(model, x_normal, x_attack, x_normal_test, track):
    print("Validating data...")
    prediction = model.predict(x_normal_test)
    score1 = np.sqrt(metrics.mean_squared_error(prediction, x_normal_test))
    prediction = model.predict(x_normal)
    score2 = np.sqrt(metrics.mean_squared_error(prediction, x_normal))
    prediction = model.predict(x_attack)
    score3 = np.sqrt(metrics.mean_squared_error(prediction, x_attack))
    print(f"Out of Sample Normal Score (RMSE): {score1}")
    print(f"Insample Normal Score (RMSE): {score2}")
    print(f"Attack Underway Score (RMSE): {score3}")

    validation_metrics = {'out_of_sample_normal_score': score1, 'in_sample_normal_score': score2,
                          'attack_underway_score': score3}
    track.log_metrics(validation_metrics)

    write_predictions_and_score(validation_metrics)
    print("Evaluation done with metrics {}.".format(json.dumps(validation_metrics)))

    write_model(model)
