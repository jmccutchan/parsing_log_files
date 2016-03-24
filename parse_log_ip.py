#!/usr/bin/python

###############################################################################################
## This file will extract the ip address from a file and return it as a dictionary data structure 
## with the line number as the key and the value as a nested dictionary with 'ip' as the key and 
## the ip address as the value
################################################################################################

import re

class Parser:

    ip_regex = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'

    output = {}

    def parse(self, filename):
        self.ip_regex=(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b')
        with open(filename) as infile:
    	    for line_number, line in enumerate(infile):
    		    result = re.search(self.ip_regex, line)
    		    if result:
    			    groups = result.group()
    			    self.output[line_number] = {}
    			    self.output[line_number]['ip'] = groups
    			    print self.output

if __name__ == "__main__":
	p = Parser()
	p.parse('logfile name')

