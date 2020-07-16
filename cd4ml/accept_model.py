import os
import mlflow
import mlflow.tracking

TENANT = os.getenv('TENANT', 'local')


def get_latest_executed_run(df_of_runs):
    filtered_dataframe = df_of_runs[df_of_runs["tags.mlflow.runName"] == os.environ["BUILD_NUMBER"]]
    print("filtered dataframe")
    print(filtered_dataframe.head())
    assert len(filtered_dataframe) == 1
    return filtered_dataframe


def get_metric(metric_name, df_of_single_run):
    print("get metric")
    print(df_of_single_run.head())
    print("Columns")
    print(list(df_of_single_run.columns))
    return df_of_single_run["attack_underway_score"].head().values[0]


def check_model_performance(metric_name, threshold_min, threshold_max):
    mlflow.set_tracking_uri(os.environ["MLFLOW_TRACKING_URL"])
    experiment = mlflow.get_experiment_by_name(TENANT)
    experiment_id = experiment.experiment_id
    print("experiment_id")
    print(experiment_id)
    runs = mlflow.search_runs(experiment_ids=experiment_id)
    print("runs")
    print(runs.head())
    last_run_record = get_latest_executed_run(runs)
    metric_value = get_metric(metric_name, last_run_record)
    run_name = last_run_record["tags.mlflow.runName"].head().values[0]
    print("run name")
    print(run_name)
    template = "Metric: {metric_name} for Run: {run_name} was not accepted, " \
               "value: {metric_value}, " \
               "threshold_min: {threshold_min}, threshold_max: {threshold_max}"
    message = template.format(run_name=run_name,
                              metric_name=metric_name,
                              metric_value=metric_value,
                              threshold_min=threshold_min,
                              threshold_max=threshold_max)

    assert threshold_min <= metric_value <= threshold_max, message
