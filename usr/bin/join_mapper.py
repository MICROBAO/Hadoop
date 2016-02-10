#!/usr/bin/env python
import sys

for line in sys.stdin:
	line=line.strip()
	key_value=line.split(',')
	key=key_value[0]
	value=key_value[1]

	if value.isdigit():
		print('%s\t%s' % (key,value))
	else:
		if value=='ABC':
			print('%s\t%s' % (key,value))
