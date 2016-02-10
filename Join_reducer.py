#!/usr/bin/env python
import sys
abc_status =False 
count=0
prev=' '

for line in f:
	line=line.strip()
	cur,value = line.split("\t",1) 
    if cur !=prev and value.isdigit():
        prev=cur
        count=0   
        abc_status =False
	if abc_status==False:
		if(value.isdigit()):
            value=int(value)
            count=count+value;
		elif value=='ABC':
            abc_status=True
            print( '%s\t%s' % (cur, count) )
