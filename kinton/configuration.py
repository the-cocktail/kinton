import os

import yaml


class Configuration:
  kinton = None
  projects = None
  aws_secrets = None

  def load():
    with open("projects.yml", 'r') as ymlfile:
        Configuration.projects = yaml.load(ymlfile)
    with open("aws_secrets.yml", 'r') as ymlfile:
        Configuration.aws_secrets = yaml.load(ymlfile)           
