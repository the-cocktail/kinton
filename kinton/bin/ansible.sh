#!/bin/bash

INVENTORY_FILE=$1
echo $@

shift
chmod +x $INVENTORY_FILE
echo "ANSIBLE_CONFIG=/tmp/kinton_ansible.cfg ansible-playbook -i ${INVENTORY_FILE} $@"

ANSIBLE_CONFIG=/tmp/kinton_ansible.cfg ansible-playbook -i ${INVENTORY_FILE} "$@"