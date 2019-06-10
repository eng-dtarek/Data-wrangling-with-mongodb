#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Here we detect the expected street types abbreviationsat any position of the name,
map it to the appropriate type, and put it at the end of the name (if it exsits at the begining).

"""
import xml.etree.cElementTree as ET
from collections import defaultdict
import re
import pprint

OSMFILE = "cairo_egypt.osm"
street_type_re = re.compile(r'\bSt\.|\bSt\.?$|\bRd\.|\bRd\.?$|\bSq\.|\bSq\.?$',re.IGNORECASE)

expected = ["Street","Square", "Road"]

mapping = { "St": "Street ",
            "St.": "Street ",
            "Sq":"Square",
            "Sq.":"Square",
            "Rd":"Road",
            "Rd.":"Road",
            "st.":"Street"
            }
'''
check if any of the expected type abbreviations exists in the name

'''
def audit_street_type(street_types, street_name):
    m = street_type_re.search(street_name)
    if m:
        street_type = m.group()
        if street_type not in expected:
            return False

    return True

'''
check if tag is a street name

'''
def is_street_name(elem):
    return (elem.attrib['k'] == "addr:street")

'''
check if tag is a way name

'''
def is_way_name(elem):
    return (elem.attrib['k'] == "name")

'''
check if tag is a way english name

'''
def is_way_en_name(elem):
    return (elem.attrib['k'] == "name:en")

'''
parse the file to find any of the type abbreviations and improve the name 
using the mapping then write the cleaned data to a new osm file  
'''
def audit(osmfile):
    osm_file = open(osmfile, "r")
    street_types = defaultdict(set)
    
    tree = ET.parse(osm_file)
    
    listtree = list(tree.iter())
    for elem in listtree:

        if elem.tag == "node" or elem.tag == "way":
            
            for tag in elem.iter("tag"):
                if is_street_name(tag):
                    if not audit_street_type(street_types, tag.attrib['v']):
                        tag.attrib['v'] = update_name(tag.attrib['v'],mapping)
                
                elif elem.tag == "way" and is_way_en_name(tag):
                    if not audit_street_type(street_types, tag.attrib['v']):
                        tag.attrib['v'] = update_name(tag.attrib['v'],mapping)

                elif elem.tag == "way" and is_way_name(tag):
                    if not audit_street_type(street_types, tag.attrib['v']):
                        tag.attrib['v'] = update_name(tag.attrib['v'],mapping)

    tree.write(osmfile[:osmfile.find('.osm')]+'_audit.osm')
    return street_types

'''
improve name by replacing the abbreviation with the correct type 
and put it at the end of the name if exists at the begining
'''
def update_name(name, mapping):
    m = street_type_re.search(name)
    if m:
        street_type = m.group()
        x=mapping[street_type]
        if name.startswith(street_type):
            filter_1=name.replace(street_type,'')
            filter_2=filter_1+' '+street_type
            name=filter_2.replace(street_type,x)
        else:
            name=name.replace(street_type,x)

    return name


def test():

    st_types = audit(OSMFILE)

    for st_type, ways in st_types.iteritems():
        for name in ways:
            better_name = update_name(name, mapping)
            print name, "=>", better_name
            

if __name__ == '__main__':
    test()