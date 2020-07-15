from sklearn import metrics
import numpy as np


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

    validation_metrics = {'Out of Sample Normal Score': score1, 'Insample Normal Score': score2,
                          'Attack Underway Score': score3}
    track.log_metrics(validation_metrics)
