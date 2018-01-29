import subprocess

class Google:
  def switch_account(google_config):
  	subprocess.run(["gcloud", "config", "set", "project", google_config["project_id"]])