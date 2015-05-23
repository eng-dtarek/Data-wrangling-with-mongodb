#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

"""
import xml.etree.cElementTree as ET
from collections import defaultdict
import re
import pprint

OSMFILE = "cairo_egypt.osm"
post_code_re=re.compile(r'\d{5}\.?$')

'''
Here we audit post codes to find any bad formatted or out of the expected range code
'''
def audit_post_code(post_code_inconsistent,post_code_error,post_code):
    m = post_code_re.match(post_code)
    if not m:
        post_code_inconsistent.add(post_code)
    else:
        cairo_post_code_range=range(11311,11669)
        cairo_post_code_range.append(11835)
        cairo_post_code_range.append(11865)
        cairo_post_code_range.append(44629)
        cairo_post_code_range.append(44635)
        cairo_post_code_range.append(44637)
        cairo_post_code_range.append(12566)

        if int(post_code) not in cairo_post_code_range:
            post_code_error.add(post_code)
            
'''
Check if tag is a post code 
'''
def is_post_code(elem):
    return (elem.attrib['k'] == "addr:postcode")

'''
Parse the file for all post code to get a list of all invalid post codes
'''
def audit(osmfile):
    results={}
    osm_file = open(osmfile, "r")
    post_code_inconsistent=set()
    post_code_error=set()
    for event, elem in ET.iterparse(osm_file, events=("start",)):

        if elem.tag == "node" or elem.tag == "way":
            for tag in elem.iter("tag"):
                if is_post_code(tag):
                    audit_post_code(post_code_inconsistent,post_code_error,tag.attrib['v'])

    results['post_code_inconsistent']=post_code_inconsistent
    results['post_code_error']=post_code_error
    return results


def test():
    
    post_code_results=audit(OSMFILE)
    pprint.pprint(post_code_results)
   
if __name__ == '__main__':
    test()