#!/bin/sh


echo pong!

#This is a temporary solution. A bash script will be called to
#deal with data and administrate the server

write_file(){

    arp -a > data_file
}


read_file(){

    cat data_file
}


if [ $1 = write ]; then
    write_file

elif [ $1 = read ]; then
    read_file
else
    echo command unknown
    exit 1
fi