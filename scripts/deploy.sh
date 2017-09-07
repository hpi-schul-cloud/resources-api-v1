#!/bin/bash

set -eO


cd "`dirname \"$0\"`"

./deploy_pypi.sh
../generators/node/generate-package.sh
