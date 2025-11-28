#!/usr/bin/python3
'''This is just a doc'''



class MyList(list):
    '''Di yazdim da'''
    
    def __init__(self):
        self.menimlistimdiyee = []
    
    def append(self, a):
        self.menimlistimdiyee += [a]
    
    def print_sorted(self):
        print(sorted(self.menimlistimdiyee))
    
    def __str__(self):
        return str(self.menimlistimdiyee)
