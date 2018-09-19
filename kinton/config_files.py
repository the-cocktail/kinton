import os
import re
import sys
import shutil
from jinja2 import Environment
from jinja2 import FileSystemLoader
from pathlib import Path
THIS_DIR = os.path.dirname(os.path.abspath(__file__))

class ConfigFiles:

  def create():
    ConfigFiles.create_files()
    ConfigFiles.create_folders()

  def create_files():
    files = ["projects.yml", "aws_secrets.yml"]
    for filename in files:   
      the_file = Path(filename)
      if the_file.exists():
        ConfigFiles.request_operation("file", filename)
      else:
        ConfigFiles.write_file(filename)

  def request_operation(type_path, resource_name):
    msg = "The {:s} {:s} exists, do you want rewrite it? (y) or (n) ".format(type_path, resource_name)
    answer = input(msg)
    if answer == "y":
      if type_path == "file":
        ConfigFiles.write_file(resource_name)
      elif type_path == "folder":
        ConfigFiles.remove_folder(resource_name)
        ConfigFiles.create_folder(resource_name)
    elif answer == "n":
      return
    else:
      ConfigFiles.request_operation(type_path, resource_name)
  
  def write_file(filename):    
    j2_env = Environment(loader=FileSystemLoader(THIS_DIR +'/templates'), trim_blocks=True)
    template = j2_env.get_template(filename + ".j2") 
    rendered_file = template.render()
    file_out = open("./" + filename, "w")
    file_out.write(rendered_file)
    file_out.close()    

  def create_folders():
    folders = ["certificates", "inventories"]
    for foldername in folders:   
      the_folder = Path(foldername)
      if the_folder.exists():
        ConfigFiles.request_operation("folder", foldername)
      else:
        ConfigFiles.create_folder(foldername)

  def create_folder(foldername):  
    path = "./" +  foldername 
    os.makedirs(path)

  def remove_folder(foldername):
    path = "./" +  foldername
    shutil.rmtree(path)