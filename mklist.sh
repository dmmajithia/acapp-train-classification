#!/bin/bash

for dir0 in $(ls -d */)
do
	for dir1 in $(ls ${dir0})
	do
		for fname in $(ls ${dir0}${dir1})
		do
			echo $(echo ${fname} | sed "s/.jpg//g"),${dir0}${dir1}/${fname} >> filelist.txt
		done
	done
done