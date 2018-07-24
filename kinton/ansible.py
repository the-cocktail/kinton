import os
import subprocess
from termcolor import cprint
from kinton.configuration import Configuration
from kinton.cloud import Cloud
from kinton.file_system import FileSystem


class Ansible:
  ANSIBLE_DIR = '/ansible/'
  SCRIPT = "/bin/ansible.sh"

  THIS_DIR = os.path.dirname(os.path.abspath(__file__))  
  INVENTORIES_DIR = os.getcwd() + "/inventories/"

  def __init__(self, project_name, ansible_config, cmd_args):
    self.project_name = project_name
    self.ansible_config = ansible_config
    self.cmd_args = cmd_args

    self.tmp_dir = Configuration.kinton["defaults"]["tmp_dir"]
    self.settings = Configuration.kinton["defaults"]["ansible"]

  def run(self):
    self.execute_command()
  
  def execute_command(self):
    inventories = self.get_inventories()
    for inventory in inventories:
      inventory_path = self.get_inventories_path() + inventory
      self.execute_command_with_inventory(inventory_path)

  def execute_command_with_inventory(self, inventory_path):
    script_path = self.THIS_DIR + self.SCRIPT
    command = ["/bin/bash", script_path, inventory_path]
  
    for arg in self.cmd_args:
      command.append(arg)

    command.append("-u")
    command.append(self.ansible_config["remote_user"])

    command.append("-e")
    command.append("ansible_user=" + self.ansible_config["remote_user"])

    command.append("-e")
    command.append("ansible_ssh_user=" + self.ansible_config["remote_user"])           

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
