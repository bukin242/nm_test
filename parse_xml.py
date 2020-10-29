#!/usr/bin/env python
import xml.etree.ElementTree as ET


accumulator = []

def nested_tags(element, level=0):

    for child in element.getchildren():
        nested_tags(child, level + 1)

    accumulator.append(level)


doc = ET.parse('xml_file.xml')
nested_tags(doc.getroot())

max_level = max(accumulator)
print max_level