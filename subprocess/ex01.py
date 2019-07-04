# coding: utf8

import subprocess

child = subprocess.Popen(["ping", "www.baidu.com"])
child.wait()
print("Parent process")