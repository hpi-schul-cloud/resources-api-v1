#!/bin/bash

set -e


cd "`dirname \"$0\"`"

./deploy-pypi.sh
../generators/node/upload.sh
