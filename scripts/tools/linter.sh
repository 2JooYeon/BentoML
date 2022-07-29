#!/usr/bin/env bash

GIT_ROOT=$(git rev-parse --show-toplevel)

cd "$GIT_ROOT" || exit 1

source ./scripts/ci/helpers.sh

INFO "(pylint) Linting bentoml..."

pylint --rcfile="./pyproject.toml" --fail-under 9.5 bentoml

INFO "(pylint) Linting examples..."

pylint --rcfile="./pyproject.toml" --fail-under 9.0 examples

INFO "(pylint) Linting tests..."

pylint --rcfile="./pyproject.toml" --disable=E0401,F0010 tests
