#!/bin/bash

if [ -z "$NPM_TOKEN" ]; then
  echo "Could not find variable NPM_TOKEN."
  exit 1
fi

echo "//registry.npmjs.org/:_authToken=$NPM_TOKEN" >> ~/.npmrc
echo "Added registry.npmjs.org to ~/.npmrc"
