# NOT STUDIED ABOUT THIS MODULE RESEARCH MORE

""" The command-line interface is also known as the CLI, which interacts with a command-line script


"""

import argparse

parser = argparse.ArgumentParser()

parser.add_argument("url", help="discription of argument 1")
parser.add_argument("output", help="by which namd do you want to save your output")

args = parser.parse_args()

print(args.url) 
""" usage: Commmand_run_in_program_argparse.py [-h] url output
Commmand_run_in_program_argparse.py: error: the following arguments are required: url, output """


print(args.output)