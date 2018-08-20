# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
a=int(input('enter no'))
root=1
diff=root*root-a
diff=abs(diff)
while(diff>=0.000001):
    root=(root+(a/root))/2
    diff=root*root-a
    print('current root',root)
    diff=abs(diff)
else:
    print(root)
