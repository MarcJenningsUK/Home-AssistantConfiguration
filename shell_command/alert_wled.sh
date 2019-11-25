#!/bin/bash

echo ${1:-7}
echo http://${2:-192.168.1.242}/json/state

result=$(wget -qO- http://${2:-192.168.1.242}/json/state)
curl --header "Content-Type: application/json" --request POST --data '{"on":true,"bri":20,"transition":7,"seg":[{"id":0,"start":0,"stop":144,"len":144,"col":[[255,0,0],[255,34,0],[0,0,0]],"fx":1,"sx":196,"ix":185,"pal":1,"sel":true,"rev":false,"cln":-1}]}' http://${2:-192.168.1.242}/json/state
sleep ${1:-7}
curl --header "Content-Type: application/json" --request POST --data $result http://${2:-192.168.1.242}/json/state

