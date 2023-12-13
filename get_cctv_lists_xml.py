'''
File: get_cctv_lists.py

Author: Lee Junseo
Created Data: 2023.12.09
Last updated: 2023.12.09

Summary:
  This file is for getting cctv lists from API and store it in cctv_lists.txt
'''

import requests
import numpy as np
import cv2
import json
import xml.etree.ElementTree as ET


cctv_lists = []

'''
function: get_cctv_lists

Summary:
    This function is for getting cctv lists from API and store it in cctv_lists.txt
    
return:
    0: success
    -1: fail
'''
def get_cctv_lists():
    minX = 127.1000
    maxX = 127.1399
    minY = 37.4321
    maxY = 37.4575

    
    f = open("datafiles/apiKey.txt", 'r')
    api_key = f.readline()
    f.close()
    
    #API call
    api_call = 'https://openapi.its.go.kr:9443/cctvInfo?'\
        'apiKey=' + api_key +\
        '&type=ex&cctvType=3'\
        '&minX='+ str(minX) +\
        '&maxX='+ str(maxX) +\
        '&minY='+ str(minY) +\
        '&maxY='+ str(maxY) +\
        '&getType=xml'
    
    response = requests.get(api_call)
    
    try:
        # Try to parse the response as XML
        root = ET.fromstring(response.text)
    except ET.ParseError:
        print(f"Failed to parse XML from response: {response.text}")
        return -1

    # Find all 'data' children within 'response'
    data_elements = root.findall('data')
    if not data_elements:
        print("No 'data' elements found in 'response'")
        return -1

    # Convert the 'data' elements into a list of dictionaries
    cctv_lists = []
    for data_element in data_elements:
        cctv = {child.tag: child.text for child in data_element}
        cctv_lists.append(cctv)


        
    if len(cctv_lists) == 0:
        print("No CCTV data in this area")
        return -1
    

    try:
        with open("datafiles/cctv_lists.txt", 'w') as f:
            for index, data in enumerate(cctv_lists):
                cctv_data = (cctv_lists[index]['cctvname'], float(cctv_lists[index]['coordy']), float(cctv_lists[index]['coordx']), cctv_lists[index]['cctvurl'])
                f.write(str(cctv_data) + "\n")
    except IOError:
        print("File open error")
        return -1
    return 0

if __name__ == "__main__":
    value = get_cctv_lists()
    if(value == -1):
        print("Failed to get cctv lists")
    else:
        print("Done")

        