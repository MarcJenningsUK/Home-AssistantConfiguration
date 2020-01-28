#!/bin/bash

# Usage:
# wled-alerter.sh 10 192.168.1.1
# where 10 is the length of time to spend flashing and 192.168.1.1 is the ip address of the WLED node.

echo ${1:-7}
server=http://${2:-192.168.3.10}/json/state
echo $server

result=$(wget -qO- $server)
curl --header "Content-Type: application/json" --request POST --data '{"on":true,"bri":21,"transition":7, "ps":-1,"pl":-1,"nl":{"on":false,"dur":60,"fade":true,"tbri":0},"udpn":{"send":false,"recv":true},"seg":[{"id":0,"start":0,"stop":144,"len":144,"col":[[0,0,255],[255,0,0],[0,0,0]],"fx":1,"sx":196,"ix":128,"pal":5,"sel":true,"rev":false,"cln":-1}]}' $server
sleep ${1:-7}
curl --header "Content-Type: application/json" --request POST --data $result $server

return 0
