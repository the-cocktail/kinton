import os
import shutil

class FileSystem:

  def create_folder(path):
    if not os.path.exists(path):
      os.makedirs(path)    

  def remove_folder(path):
    shutil.rmtree(path)