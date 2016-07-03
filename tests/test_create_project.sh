#!/bin/bash

set -e

require() {
    type $1 >/dev/null 2>/dev/null
}

cleanup() {
    rm -rf python-boilerplate
}
trap cleanup EXIT


require cookiecutter

echo "Running test script..."
cookiecutter . --no-input
(
    cd ./python-boilerplate
    make install-reqs
    make check-setup docs-build
    make test dist

    pip install cryptography pyyaml
    python travis_pypi_setup.py --repo audreyr/cookiecutter-pypackage --password invalidpass
    python -c '''import yaml
assert "secure" in yaml.load(open(".travis.yml"))["deploy"]["password"],\
    ".travis.yml missing password config"'''
)

echo Done
