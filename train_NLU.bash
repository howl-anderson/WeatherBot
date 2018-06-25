#!/usr/bin/env bash

python -m rasa_nlu.train -c nlu_model_config.yaml -d nlu.json --fixed_model_name current -o models
