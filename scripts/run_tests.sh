#!/usr/bin/env bash
set -e
project_path=$(dirname $0)/..

export PYTHONPATH=$project_path

coverage run --source='./mock_data_generator' --omit='*/tests/*' -m pytest
coverage report -m
