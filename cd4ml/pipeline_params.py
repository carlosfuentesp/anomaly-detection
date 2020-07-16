# parameters for running the pipeline
from cd4ml.model_params import model_parameters

pipeline_params = {'model_name': 'autoencoders',
                   'acceptance_metric': 'attack_underway_score',
                   'acceptance_threshold_min': 0.0,
                   'acceptance_threshold_max': 0.5,
                   'model_params': model_parameters
                   }
