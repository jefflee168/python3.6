# coding: utf8

import subprocess

def run_command(command):
    command = command.rstrip()
    try:
        child = subprocess.check_output(command, shell=True)
    except:
        child = 'Can not execute the command.\r\n'
    return child

execute = "dir c:"
output = run_command(execute)
print(output)