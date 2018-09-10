import os
import datetime
from pathlib import Path
from jinja2 import Environment
from jinja2 import FileSystemLoader

THIS_DIR = os.path.dirname(os.path.abspath(__file__))

class Aws:
  def switch_account(aws_config):
    j2_env = Environment(loader=FileSystemLoader(THIS_DIR +'/templates'), trim_blocks=True)
    template = j2_env.get_template('aws_credentials.j2') 

    rendered_file = template.render(aws_access_key_id=aws_config["aws_access_key_id"], 
                                    aws_secret_access_key=aws_config["aws_secret_access_key"],
                                    region=aws_config["region"],
                                    now=datetime.datetime.utcnow())
    home_path = str(Path.home())
    file_out = open(home_path + "/.aws/credentials", "w")
    file_out.write(rendered_file)
    file_out.close()
