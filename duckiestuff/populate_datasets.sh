#!/bin/bash
dirs=(201 202)

rm -rf trainset
rm -rf testset
mkdir trainset
mkdir testset

for dir in ${dirs[@]}; do
	for file in `ls train_data/$dir/`; do
		cp train_data/$dir/$file "trainset/${dir}_$file" 
	done
done

for file in `ls train_data/203/`; do
	cp train_data/203/$file testset/203_$file
done

