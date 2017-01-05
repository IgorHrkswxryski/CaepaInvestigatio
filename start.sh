#!/bin/bash

# More easier to detect errors ;)
set -x

# install go
bash < <(curl -s -S -L https://raw.githubusercontent.com/moovweb/gvm/master/binscripts/gvm-installer)
[[ -s "$HOME/.gvm/scripts/gvm" ]] && source "$HOME/.gvm/scripts/gvm"
source /$HOME/.gvm/scripts/gvm
gvm install go1.7 --binary
gvm use go1.7

# download et install onionscan
go get github.com/s-rah/onionscan
go install github.com/s-rah/onionscan

# we need tiedot db to read crawls
mkdir tiedot && cd tiedot
export GOPATH=`pwd`  # backticks surround pwd
go get github.com/HouzuoGuo/tiedot

# tor hash
tor --hash-password coucou > torhash

# configure tor
printf "ControlPort 9051\nControlListenAddress 127.0.0.1\nHashedControlPassword %s" $(tail -n 1 torhash) >> /etc/tor/torrc

#Restart TOR socket
/etc/init.d/tor restart

# create virtualenv
#export VIRTUALENV_PATH="/tmp/virtualenv_caepainvestigation"
#virtualenv ${VIRTUALENV_PATH}
#${VIRTUALENV_PATH}/bin/activate

# install our package
python setup.py build
python setup.py develop

