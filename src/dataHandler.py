
import xml.etree.ElementTree as ET

import requests



def readData(test=False):
    if test:
        url = 'https://alerts.fmi.fi/cap/feed/2023/11-12/12-48-01Z-atom_fi-FI.xml'
    else:
        url = 'https://alerts.fmi.fi/cap/feed/atom_fi-FI.xml'

    # creating HTTP response object from given url
    resp = requests.get(url)

    # saving the xml file
    with open('weather_alerts.xml', 'wb') as f:
        f.write(resp.content)


def parseXML(xmlfile):
    alerts = []

    # create element tree object
    tree = ET.parse(xmlfile)
    # get root element
    root = tree.getroot()
    entries = find_elements("entry", root)

    for i in entries:
        info = find_elements("info", i, "content/alert")
        for j in info:
            if j[0].text == "fi-FI":
                info = j

        alerts.append({
            "title": find_elements("title", i)[0].text,
            "event": find_elements("event", info)[0].text,
            "urgency": find_elements("urgency", info)[0].text,
            "certainty": find_elements("certainty", info)[0].text,
            "description": find_elements("description", info)[0].text,
            "areas": [x[0].text for x in find_elements("area", info)]
        })

    return alerts

def find_elements(tag, root_element, path=None):
    elements_found = []

    if path != None and path != "":
        tags = path.split("/")
        xtag = tags.pop(0)
        match = False
        count = 0
        while not match:

            if xtag in root_element[count].tag:
                elements_found = find_elements(tag, root_element[count], "/".join(tags))
                match = True
            else:
                count += 1
    else:
        for i in root_element:
            if tag in i.tag:
                elements_found.append(i)
    return elements_found