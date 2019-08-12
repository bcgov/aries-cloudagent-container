#!/bin/sh

cd $HOME

if ! python -c "from indy import crypto, did, pairwise, wallet"; then
    echo "Importing indy module failed"
fi

if ! python -c "import aries_cloudagent"; then
    echo "Importing aries-cloudagent module failed"
fi
