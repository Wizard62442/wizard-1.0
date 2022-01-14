#!/bin/bash

echo -e "\033[1;33;40m[~] CHECKING DEPENDENCIES... \033[0m"


echo -e "\033[1;33;40m[~] UPDATING..\033[0m"
apt update

echo -e "\033[1;33;40m[~] UPGRADING..\033[0m"
apt upgrade

apt install metasploit-framework
echo -p "\033[1;34;40mTYPE python main.py to run tool :) \033[0m"
