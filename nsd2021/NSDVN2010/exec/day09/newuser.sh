#!/bin/bash
for ip in `cat blog | awk '{print $1)'`
do
	cat alog | grep ^${ip} &> /dev/null
	if [ $? -ne 0 ];then
		echo ${ip}
	fi
done

run:  bash newuser.sh | sort -u