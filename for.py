#!/usr/bin/env python3
#-*-coding-utf-8-*-
name=['peng','yin','yang','鹏']
for i in name:
	print('Hello:%s!'% i)
sum=0
for i in range(101):
	if i % 2!=0:
		continue
	sum=sum+i
print(sum)
