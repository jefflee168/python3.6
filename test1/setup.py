# coding: utf8

from distutils.core import setup
import py2exe

options = {
    # 打包成一个 exe 文件
    "bundle_files" : 1,
    # 压缩
    "compressed" : 1,
    "optimize" : 2,
}

setup (
    options = options,
    zipfile=None,
    console = ["backdoorclient.py"]
)
