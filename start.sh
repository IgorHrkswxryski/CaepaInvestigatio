#!/bin/bash

bash < <(curl -s -S -L https://raw.githubusercontent.com/moovweb/gvm/master/binscripts/gvm-installer)
[[ -s "$HOME/.gvm/scripts/gvm" ]] && source "$HOME/.gvm/scripts/gvm"
source /root/.gvm/scripts/gvm
gvm install go1.4 --binary
gvm use go1.4

go get github.com/s-rah/onionscan
go install github.com/s-rah/onionscan


tor --hash-password coucou53 > torhash

# configure tor
printf "ControlPort 9051\nControlListenAddress 127.0.0.1\nHashedControlPassword %s" | cat torhash >> /etc/tor/torrc

#Restart TOR socket
service tor restart

# create virtualenv
export VIRTUALENV_PATH="/tmp/virtualenv_caepainvestigation"

virtualenv --python python3 VIRTUALENV_PATH
.${VIRTUALENV_PATH}/bin/activate

python setup.py develop
