user_id=`nvidia-smi |grep MiB|grep -v %|awk -v ORS=, '{print $3}'|sed -e 's/\(.\+\),/\1/g'`
top -p ${user_id}
