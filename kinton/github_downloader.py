import os
import shutil
import subprocess
from github import Github
from github import GithubException
from kinton.configuration import Configuration
from kinton.file_system import FileSystem

class GithubDownloader:
  
  def __init__(self, github_config):
    self.github = Github(Configuration.kinton["github_token"])
    organization = self.github.get_organization(github_config["organization"])
    self.repository = organization.get_repo(github_config["respository"])

    self.tmp_dir = Configuration.kinton["defaults"]["tmp_dir"]
  
  def get_folder(self, folder_path, sha="master", exclude_dirs=[]):
    path = self.tmp_dir + folder_path
    FileSystem.create_folder(path)
    self.download_folder(folder_path, sha, exclude_dirs)

  def download_folder(self, folder_path, sha ,exclude_dirs):
    contents = self.repository.get_dir_contents(folder_path, ref=sha)
    
    for content in contents:
      if content.type == 'dir':
        folder_name = content.path.split("/")[-1]
        if folder_name not in exclude_dirs:
          self.create_folder(content.path)
          self.get_folder(content.path, sha, exclude_dirs)
      else:
        try:
          path = content.path
          file_content = self.repository.get_contents(path, ref=sha)
          file_data = file_content.decoded_content.decode('utf-8')
          output_path = self.tmp_dir + content.path
          file_out = open(output_path, "w")
          file_out.write(file_data)
          file_out.close()
        except (GithubException, IOError) as exc:
          print('Error processing %s: %s', content.path, exc)

  def create_folder(self, folder=""):
    path = self.tmp_dir + folder
    FileSystem.create_folder(path)