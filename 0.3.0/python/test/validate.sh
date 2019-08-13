#!/bin/sh

cd $HOME

if ! python -c "import aries_cloudagent"; then
    echo "Importing aries-cloudagent module failed"
fi
