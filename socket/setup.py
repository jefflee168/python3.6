# coding: utf8

from distutils.core import setup
import py2exe

options = {
    # 设置是否打包 3 默认不打包; 2 打包，但不打包python 解释器；1 打包，包括 python 解释器
    "bundle_files" : 1,
    # 设置是否压缩库文件，1 压缩，2不压缩
    "compressed" : 1,
    # 代码优化，0 不优化，1 一般优化， 2 额外优化
    "optimize" : 2,
}

setup (
    # 要转换为 console exe 的代码列表
    windows = ["client02.py"],
    # 设置编码时需要的选项
    options = {"py2exe": options},
    # 将运行需要的模块打包为 zip 文件。 None 表示只打包可执行文件
    zipfile = None
)