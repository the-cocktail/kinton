from setuptools import setup

setup(name='kinton',
      version='0.2.0',
      description='This is the perfect tool if you want run the same tasks in servers in AWS and Google Cloud with only one comand.',
      long_description="Kinton is a software that automates software provisioning and configuration management when you have servers in different cloud computing providers or in different cloud computing accounts in the same provider. This is the perfect tool if you want run the same tasks in servers in AWS and Google Cloud with only one comand.",
      classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Operating System :: Unix',
        'Intended Audience :: System Administrators',
        'Topic :: System :: Systems Administration',
      ],      
      keywords='ansible infrastructure provisioning',
      url='https://github.com/the-cocktail/kinton',
      author='Jesus Sayar',
      author_email='jesus.sayar@the-cocktail.com',
      license='MIT',
      packages=['kinton'],
      install_requires=[
          'PyYAML==3.12',
          'ipdb==0.10.3',
          'termcolor==1.1.0',
          'pygithub==1.35',
          'Jinja2==2.9.6'
      ],
      entry_points = {
        'console_scripts': ['kinton=kinton.command_line:main'],
      },      
      include_package_data=True,
      zip_safe=False)
