#!/bin/bash

touch .env
declare -a env_vars=(
  "DB_DIRECTORY"
)

for var_name in "${env_vars[@]}"; do
    if [ ! -z ${!var_name+x} ]; then
        echo "$var_name=${!var_name}" >> .env
    fi
done

python main.py
