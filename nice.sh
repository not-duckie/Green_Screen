#!/bin/bash
touch ip.html
netstat -antp|awk '{print $5}'|grep  '[0-9.]'|cut -d":" -f1|sort -u|uniq -u>>ip.html
for ip in $(cat ip.html);do
echo $ip
a=`python -c 'print "="*80'`
echo $a
done;
rm -r ip.html;
