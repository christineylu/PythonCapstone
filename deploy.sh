#!/usr/bin/env bash

cd simple-react
npm run-script build
cd -

# for prod
# git tag -a "v1.0.2" -m "Minor revision to homepage."
# eb deploy -l "eb-flask-app v1.0.2"

# for dev
eb deploy

