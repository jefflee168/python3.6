#!/bin/bash
  
cpu_idle=$(top -n2 | grep 'Cpu' | tail -n 1 | awk '{ print $8 }')
cpu_usage=$(echo "100 - $cpu_idle " | bc)

mem_free=$(free -m | grep 'Mem:' | awk '{ print $4 }')
mem_total=$(free -m | awk '/Mem:/{ print $2 }')
mem_used=$(echo "$mem_total - $mem_free" | bc)
mem_rate=$(echo "$mem_used * 100 / $mem_total" | bc)

disk_total=$(df -h / | tail -n 1 | awk '{ print $2 }')
disk_usage=$(df -h / | tail -n 1 | awk '{ print $5 }')
disk_used=$(df -h / | tail -n 1 | awk '{ print $3 }')

echo "cpu利用率: $cpu_usage %"
echo "内存总数：$mem_total M"
echo "内存使用量: $mem_used M"
echo "内存利用率：$mem_rate %"
echo "硬盘总空间：$disk_total"
echo "硬盘空间使用量：$disk_used"
echo "磁盘空间利用率：$disk_usage"

cat << EOF
<html>
    <head></head>
    <body>
	<table>
	    <tr><td>cpu利用率: $cpu_usage %</td></tr>
	    <tr><td>内存总数：$mem_total M</td></tr>
	    <tr><td>内存使用量: $mem_used M</td></tr>
	    <tr><td>内存利用率：$mem_rate %</td></tr>
	    <tr><td>硬盘总空间：$disk_total</td></tr>
	    <tr><td>硬盘空间使用量：$disk_used</td></tr>
	    <tr><td>磁盘空间利用率：$disk_usage</td></tr>
	</table>
    </body>
</html>
EOF
