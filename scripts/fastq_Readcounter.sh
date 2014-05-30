#!/bin/bash

while read LINE; do
	echo number of Reads \(lines\/4\) in File ${LINE};		
	wc -l ${LINE} | cut -f1 -d' '|echo $(($(cat)/4));
done
exit
