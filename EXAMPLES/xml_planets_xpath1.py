# import xml.etree.ElementTree as ET
import lxml.etree as ET

doc = ET.parse('../DATA/solar.xml')  # parse XML file

planets = doc.findall('.//planet')

for planet in planets:  # loop through search results
    print(planet.get("planetname"))  # print "name" attribute of planet element
    for moon in planet.findall('moon'):
        print(f"\t{moon.text}")
