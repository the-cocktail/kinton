#!/bin/bash

ANSIBLE_DIR=$1
INVENTORY_FILE=$2

shift
shift
cd $ANSIBLE_DIR
chmod +x $INVENTORY_FILE
echo "ansible-playbook -i ${INVENTORY_FILE} $@"

ansible-playbook -i ${INVENTORY_FILE} "$@"