# Kinton

## What is it

Kinton is a software that automates software provisioning and configuration management when you have servers in different cloud computing providers or in different cloud computing accounts in the same provider. This is the perfect tool if you want run the same tasks in servers in AWS and Google Cloud with only one comand.

### How it work
Kinton accesses the GitHub repositories of your projects and downloads its Ansible code. Then use your inventory files to recover the ips of your servers and execute operations on them. That's why he needs a list of your GitHub projects with information about his Ansible configuration. Kinton executes the Ansible inventories of your projects to obtain the ips of your servers, for that reason it needs the AWS credentials of each project.

## Installation

`pip install kinton`

## Configuration

Init configuration files.

`kinton init`

Then you can complete this files with your configuration:

### kinton.yml

This file have the basic settings.

| Key  | Description |
| ---  | ----------- |
| github_token | Your GitHub token.  |
| defaults.tmp_dir  | Temporary folder used by Kinton. |
| defaults.ansible.exclude_dirs  | Excluded folders when Kinton download the ansible folder from your repositories. |


### projects.yml

This file contains a list with all projects that you want management.

| Key  | Description |
| ---  | ----------- |
| project_name  | Descriptive project name.  |
| enabled  | If `True` this projects is management, if `False` the project is not management. |
| github.organization  | GitHub Organization name of your respository. |
| github.respository  | GitHub Repository name. |
| ansible.remote_user  | Remote user used in your servers. |
| ansible.ansible_dir  | Relative path to ansible config folder in the repository. |
| ansible.inventories  | Relative paths to the Ansible enventory files in the ansible directory. This determine which server provision. |
| ansible.cloud.aws  | If you use AWS cloud platform. |
| ansible.cloud.google  | If you use Google Cloud platform. |
| ansible.cloud.google.project_id  | Project ID in the Google Cloud platform. |


This is a basic example for a fictitious project hosted in https://github.com/the-cocktail/fictitious_app.

```
fictitious_app:
  enabled: True
  github:
    organization: "the-cocktail"
    respository: "fictitious_app"
  ansible:
    remote_user: "ubuntu"
    ansible_dir: "infrastructure/ansible"
    inventories:
      - "staging/inventory"
      - "production/inventory"       
  cloud:
    aws:
```

### aws_secrets.yml

If you have servers in AWS you need this file with the API credentials.

| Key  | Description |
| ---  | ----------- |
| project_name  | Descriptive project name, this name should be equal to name used in the projects.yml file |
| aws_access_key_id | AWS access key |
| aws_secret_access_key | AWS secret access key|
| region | AWS region used for your servers|

```
fictitious_app:
  aws_access_key_id: "XXX"
  aws_secret_access_key: "XXX"
  region: "eu-west-1"
```

## How use it

You can use it, how you use Ansible, you can pass any Ansible argument and Kinton will use it.

`kinton playbook.yml --tags 'nginx'`