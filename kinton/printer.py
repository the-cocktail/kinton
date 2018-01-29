from termcolor import cprint

class Printer:
  def __init__(self, project):
    self.project = project

  def puts_basic_info(self):
    self.puts_project()
    self.puts_cloud()

  def puts_project(self):
    cprint("PROJECT: " + self.project["name"], "blue")
  
  def puts_cloud(self):
    if "aws" in self.project["cloud"]:
      cloud = "AWS"
    elif "google" in self.project["cloud"]:
      cloud = "GOOGLE"
    
    cprint("CLOUD: " + cloud, "blue")      