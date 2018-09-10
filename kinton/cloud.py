import subprocess
import datetime
from kinton.aws import Aws
from kinton.google import Google
from kinton.configuration import Configuration

class Cloud:
  def __init__(self, project_config):
    self.project_config = project_config

  def configure(self):
    if "aws" in self.project_config["cloud"]:
      aws_config = Configuration.aws_secrets[self.project_config["cloud"]["aws"]]
      Aws.switch_account(aws_config)
    elif "google" in self.project_config["cloud"]:
      google_config = self.project_config["cloud"]["google"]
      Google.switch_account(google_config)
