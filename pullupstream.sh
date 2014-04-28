#!/bin/bash

git remote add upstream https://github.com/klen/python-mode.git
git checkout -t -b develop origin/develop
git pull upstream develop
