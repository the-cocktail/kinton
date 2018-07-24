#!/bin/bash

INVENTORY_FILE=$1
echo $@

shift
chmod +x $INVENTORY_FILE
#echo "ansible-playbook -i ${INVENTORY_FILE} $@"

ansible-playbook -i ${INVENTORY_FILE} "$@"