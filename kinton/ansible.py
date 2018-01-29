import os
import subprocess
from termcolor import cprint
from kinton.configuration import Configuration
from kinton.cloud import Cloud
from kinton.file_system import FileSystem


class Ansible:
  ANSIBLE_DIR = '/ansible/'
  PLAYBOOK_FILE = "playbook.yml"
  SCRIPT = "/bin/ansible.sh"

  THIS_DIR = os.path.dirname(os.path.abspath(__file__))  

  def __init__(self, ansible_config, downloader, cmd_args):
    self.ansible_config = ansible_config
    self.downloader = downloader
    self.cmd_args = self.parse_args(cmd_args)

    self.tmp_dir = Configuration.kinton["defaults"]["tmp_dir"]
    self.settings = Configuration.kinton["defaults"]["ansible"]

  def run(self):
    self.create_temp_folder()
    self.download_temp_files()
    self.execute_command()
    self.remove_temp_folder()

  def create_temp_folder(self):
    FileSystem.create_folder(self.tmp_dir)

  def download_temp_files(self):
    exclude_dirs = self.settings["exclude_dirs"]
    if "exclude_dirs" in self.ansible_config:
      exclude_dirs += self.ansible_config["exclude_dirs"]
    self.downloader.get_folder(self.ansible_config["ansible_dir"], exclude_dirs=exclude_dirs)
  
  def execute_command(self):
    for inventory in self.ansible_config["inventories"]:
      ansible_dir = self.tmp_dir + self.ansible_config['ansible_dir']
      script_path = self.THIS_DIR + self.SCRIPT
      command = ["/bin/bash", script_path, ansible_dir, inventory]
    
      for arg in self.cmd_args:
        command.append(arg)

      command.append("-u")
      command.append(self.ansible_config["remote_user"])
            
      subprocess.run(command)

  def remove_temp_folder(self):
    FileSystem.remove_folder(self.tmp_dir)

  def parse_args(self, cmd_args):
    for index, item in enumerate(cmd_args):
      if item.endswith(".yml"):
        current_path = os.getcwd()
        cmd_args[index] = current_path +  "/" + item
    return cmd_args
