from cd4ml.pipeline_helpers import run_ml_pipeline


def main(*args):
    """
    Run the pipeline
    """
    args = args[0]
    if len(args) > 0:
        variable = args[0]
    else:
        variable = None

    if variable:
        print('variable: %s' % variable)

    run_ml_pipeline()
