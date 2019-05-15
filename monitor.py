# coding: utf8

from __future__ import unicode_literals
import psutil

def bytes2human(n):
    symbols = ('K','M','G','T','P','E','Z','Y')
    prefix = {}
    for i, s in enumerate(symbols):
        prefix[s] = 1 << (i + 1) * 10
    for s in reversed(symbols):
        if n >= prefix[s]:
            value = float(n) / prefix[s]
            return '%.1f%s' % (value, s)
    return  "%sB" % n

# cpu_idle =
cpu_usage = psutil.cpu_percent(interval=1)

virtual_mem = psutil.virtual_memory()
#mem_free = bytes2human(virtual_mem.free + virtual_mem.buffers + virtual_mem.cached)
mem_total = bytes2human(virtual_mem.total)
mem_rate = virtual_mem.percent
mem_used = bytes2human(virtual_mem.total * (virtual_mem.percent / 100))

disk_space = psutil.disk_usage('/')
disk_total = bytes2human(psutil.disk_usage('/').total)
disk_usage = psutil.disk_usage('/').percent
disk_used = bytes2human(psutil.disk_usage('/').used)
disk_idle = bytes2human(disk_space.total - disk_space.used)

print("cpu利用率: ", cpu_usage,'%')
print("内存总数：", mem_total)
print("内存使用量: ", mem_used)
print("内存利用率：", mem_rate, '%')
print("硬盘总空间：", disk_total)
print("硬盘空间使用量: ", disk_used)
print("磁盘空间利用率：", disk_usage, '%')
print("磁盘剩余空间： ", disk_idle)