import sys
from kinton.configuration                    import Configuration
from kinton.cloud                            import Cloud
from kinton.ansible                          import Ansible
from kinton.printer                          import Printer
from kinton.config_files                     import ConfigFiles


def main():
  args = sys.argv[1:]
  if (len(args) == 1) and (args[0]=="init"):
    ConfigFiles.create()
  else:
    Configuration.load()
    execute_ansible(args)

def execute_ansible(args):
  projects = get_projects() 

  for project in projects:
    printer = Printer(project)
    printer.puts_basic_info()
    cloud = Cloud(project)
    cloud.configure()

    ansible = Ansible(project["name"], project["ansible"], args)
    ansible.run()

def get_projects():
  projects = []
  for key, data in Configuration.projects.items():
    if ("enabled" not in data) or (data["enabled"] == True):
      data["name"] = key
      projects.append(data)
  return projects

if __name__ == "__main__":
  main()
