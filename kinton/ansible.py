import os
import subprocess
from termcolor import cprint
from kinton.configuration import Configuration
from kinton.cloud import Cloud
from kinton.file_system import FileSystem
from kinton.ansible_config import AnsibleConfig

class Ansible:
  ANSIBLE_DIR = '/ansible/'
  SCRIPT = "/bin/ansible.sh"

  THIS_DIR = os.path.dirname(os.path.abspath(__file__))  
  INVENTORIES_DIR = os.getcwd() + "/inventories/"

  def __init__(self, project_name, config, cmd_args):
    self.project_name = project_name
    self.config = config
    self.cmd_args = cmd_args

  def run(self):
    self.execute_command()
  
  def execute_command(self):
    inventories = self.get_inventories()
    for inventory in inventories:
      inventory_path = self.get_inventories_path() + inventory
      ansible_config = AnsibleConfig(inventory_path, self.config["remote_user"])
      ansible_config.create()
      self.execute_command_with_inventory(inventory_path, ansible_config.exists_bastion())
      ansible_config.delete()

  def execute_command_with_inventory(self, inventory_path, exists_bastion):
    script_path = self.THIS_DIR + self.SCRIPT
    command = ["/bin/bash", script_path, inventory_path]
  
    for arg in self.cmd_args:
      command.append(arg)

    certificate_path = "certificates/" + self.project_name + ".pem"
    if os.path.exists(certificate_path):
      current_path = os.getcwd()
      command.append("--private-key=" +  current_path + "/" + certificate_path)  
    
    subprocess.run(command)

  def get_inventories(self):
    from os import listdir
    from os.path import isfile, join
    inventories_path = self.get_inventories_path()
    onlyfiles = [f for f in listdir(inventories_path) if isfile(join(inventories_path, f))]

    return onlyfiles


  def get_inventories_path(self):
    return self.INVENTORIES_DIR + self.project_name + "/"

  def parse_args(self, cmd_args):
    for index, item in enumerate(cmd_args):
      if item.endswith(".yml"):
        current_path = os.getcwd()
        cmd_args[index] = current_path +  "/" + item
    return cmd_args
