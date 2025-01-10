#!/bin/sh

cd $HOME

if ! python -c "import acapy_agent"; then
    echo "Importing acapy-agent module failed"
    exit 1
fi
