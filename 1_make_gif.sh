#! /bin/bash
##Tue Jun 10 11:04:47 CEST 2014

for i in 1 2 3 4 5 6 7 8
do
convert  -delay 150 -loop 0 'ch'$i'/ch'$i'Distance_*.png' 'ch'$i'/ch'$i'_animated.gif';
cp 'ch'$i'/ch'$i'_animated.gif' 'only_gifs/ch'$i'_animated.gif';
echo -ne "Done with chromosome $i \n"
done;

