#!/usr/bin/env bash

python -m rasa_core.run -d models/dialogue -u models/default/current \
       --port 5002 --credentials credentials.yml \
       --cors * --endpoints endpoints.yml