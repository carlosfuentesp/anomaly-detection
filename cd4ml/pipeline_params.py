# parameters for running the pipeline
from cd4ml.model_params import model_parameters

pipeline_params = {'model_name': 'autoencoders',
                   'acceptance_metric': 'attack_underway_score',
                   'acceptance_threshold_min': 0.4,
                   'acceptance_threshold_max': 1.0,
                   'model_params': model_parameters
                   }
