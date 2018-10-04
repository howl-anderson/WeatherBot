#!/usr/bin/env bash

python -m rasa_core.train -s stories.md -d domain.yml -o models/dialogue --epochs 500 --endpoints endpoints.yml
