#!/usr/bin/env python

import requests
import sys
import json

def check_argument():
    'Funtion to check if the number of arguments match correctly'
    try:
        arg_list = sys.argv
        length = len(sys.argv)
        #print('Length is', length)
        # print('Argument list is:',arg_list)
        if length==2:
            #print('The argument passed is :', arg_list[1])
            search(arg_list[1])
        else:
            print('Number of arguments passed are incorrect, Please pass the the mac address along with script name  ')
    except Exception as e:
        print('Exception',e)

def search(mac_address):
    'Function to check the MAC address online'
    try:
        company=""
        myurl = 'https://api.macaddress.io/v1?apiKey=at_mNAGqWbXKQMn2hxfpLz6pWlmUNkNo&output=json&search='
        search_url = myurl + mac_address
        print search_url
        request = requests.get(search_url)
        status_code = request.status_code
        if status_code == 200:
            api_result = request.text
            utf_string = api_result.encode("utf-8")
            res = json.loads(utf_string)
            #vendor = res[u'vendorDetails']
            #company = vendor[u'companyName']
            company=res['vendorDetails']['companyName']
            print('The Company Name is',company)
        else:
            print('There is no company associated given MAC address')
    except Exception as e:
        print('Exception',e)

if __name__=="__main__":
    try:
        check_argument()
    except Exception as e:
        print('Exception',e)
