import os
import re
import sys
from jinja2 import Environment
from jinja2 import FileSystemLoader
from pathlib import Path
THIS_DIR = os.path.dirname(os.path.abspath(__file__))

class ConfigFiles:
  def create():
    files = ["kinton.yml", "projects.yml", "aws_secrets.yml"]
    for filename in files:   
      the_file = Path(filename)
      if the_file.exists():
        ConfigFiles.request_operation(filename)
      else:
        ConfigFiles.write_file(filename)

  def request_operation(filename):
    msg = "The file {:s} exists, do you want rewrite it? (y) or (n) ".format(filename)
    answer = input(msg)
    if answer == "y":
      ConfigFiles.write_file(filename)
    elif answer == "n":
      return
    else:
      ConfigFiles.request_operation(filename)
  
  def write_file(filename):    
    j2_env = Environment(loader=FileSystemLoader(THIS_DIR +'/templates'), trim_blocks=True)
    template = j2_env.get_template(filename + ".j2") 
    rendered_file = template.render()
    file_out = open("./" + filename, "w")
    file_out.write(rendered_file)
    file_out.close()    

