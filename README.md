# snapshot-analyzer-30000
Demo project to list EC2 snapshots

###About

This project is from ACLOUD GURU's python class where you can list out your EC2 instances. 
It uses boto3 package for python.
Everything is created inside "pipenv"
"shotty" is the name of the config file created for AWS CLI.
'aws configure --profile shotty'

#running
pipenv run python shotty/shotty.py

Added more commands on CLI using CLICK module for python. Using BOTO3 module to manage EC2 instances.

Using Click module following commands are added:
1. List - List all the EC2 instance, their status and more. 
2. Start
3. Stop

pipenv run python shotty/shotty.py --help

pipenv run python shotty/shotty.py list

pipenv run python shotty/shotty.py start

pipenv run python shotty/shotty.py stop


