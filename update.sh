#!/bin/bash

SALT='dns.memair.com'
DATE=`date '+%Y-%m-%d'`
HASH=`echo -n $DATE$SALT | md5sum | awk '{print $1}'`
HASH_END=$((16#${HASH: -1}))

if [ $((HASH_END%2)) -eq 0 ];
then
    echo "even day, allowing social media";
    sed -i '/memair/s/^#*/#/g' /etc/pihole/adlists.list
else
    echo "odd hash day, disallowing social media";
    sed -i '/memair/s/^#*//g' /etc/pihole/adlists.list
fi

echo "refreshing pihole lists"
pihole -g
