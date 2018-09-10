from jinja2 import Environment
from jinja2 import FileSystemLoader
import subprocess
import os
import json
import ipdb

class AnsibleConfig:
  THIS_DIR = os.path.dirname(os.path.abspath(__file__))
  ANSIBLE_CONFIG_PATH = '/tmp/kinton_ansible.cfg'
  SSH_CONFIG_PATH = '/tmp/kinton_ssh.cfg'

  def __init__(self, inventoy_path, remote_user):
    self.inventoy_path = inventoy_path
    self.remote_user = remote_user
    self.server_ips = self.get_server_ips()
  
  def create(self):
    self.create_ansible_config()
    self.create_ssh_config()

  def create_ansible_config(self):
    j2_env = Environment(loader=FileSystemLoader(self.THIS_DIR +'/templates'), trim_blocks=True)
    template = j2_env.get_template('ansible.cfg.j2') 

    rendered_file = template.render(ssh_config_path=self.SSH_CONFIG_PATH) 
    file_out = open(self.ANSIBLE_CONFIG_PATH, "w")
    file_out.write(rendered_file)
    file_out.close()

  def create_ssh_config(self):
    j2_env = Environment(loader=FileSystemLoader(self.THIS_DIR +'/templates'), trim_blocks=True)
    if self.exists_bastion():
      template = j2_env.get_template('ssh_bastion.cfg.j2') 
      rendered_file = template.render(ssh_config_path=self.SSH_CONFIG_PATH, bastion_ip=self.server_ips["bastion"][0],remote_user=self.remote_user) 
    else:
      template = j2_env.get_template('ssh.cfg.j2') 
      rendered_file = template.render(ssh_config_path=self.SSH_CONFIG_PATH, remote_user=self.remote_user)
    file_out = open(self.SSH_CONFIG_PATH, "w")
    file_out.write(rendered_file)
    file_out.close()

  def get_server_ips(self):
    result = subprocess.run([self.inventoy_path], stdout=subprocess.PIPE)
    print(result.stdout.decode("utf-8"))
    data = json.loads(result.stdout.decode("utf-8"))
    return data

  def exists_bastion(self):
    if 'bastion' in self.server_ips:
      return True
    else:
      return False

  def delete(self):
    if os.path.exists(self.ANSIBLE_CONFIG_PATH):
      os.remove(self.ANSIBLE_CONFIG_PATH)
    if os.path.exists(self.SSH_CONFIG_PATH):
      os.remove(self.SSH_CONFIG_PATH)      
